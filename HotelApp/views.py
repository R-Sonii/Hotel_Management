import datetime

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from HotelApp.models import Guest, Bookings, Rooms, Visitor, Visitor_list

# This is to add Guest
from HotelApp.serializer import BookingsSerializer, VisitorSerializer


def addGuest(request):
    if request.method == "POST":
        room_number = request.POST.get('room_number')

        result = Rooms.objects.filter(room_number=room_number, reserved_room="No")
        if not result:
            return HttpResponse("Room Not Available")
        people = request.POST.get('people')
        amount = request.POST.get('amount')
        contact = request.POST.get('contact')
        firstName = request.POST.get('fname')
        lastName = request.POST.get('lname')
        email = request.POST.get('email')
        idtype = request.POST.get('idtype')
        idnumber = request.POST.get('idnumber')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        print('hi')
        # This is to check that none of the above fields are blank
        if contact and firstName and lastName and email and idtype and idnumber and address and city and state:

            check = Guest.objects.filter(contact=contact)
            # This is to check that customer already exists
            if check:
                cust_id = check[0].id
            else:
                data = Guest(firstName=firstName, lastName=lastName, contact=contact, email=email, idtype=idtype,
                             idnumber=idnumber, address=address, city=city, state=state)
                data.save()
                # data=Guest.object.all()
                cust_id = Guest.objects.latest('id').id

            roomObject = Rooms.objects.get(room_number=room_number)
            room_id = roomObject.id
            status = savebooking(cust_id, room_id, people, amount)
            if status == 'success':
                return HttpResponse('success')
            else:
                return HttpResponse("Failed")
        else:
            return HttpResponse("Invalid Data")
    else:
        return JsonResponse({'err': 'error'})


def currentGuest(request):
    if request.method == "GET":
        data = Bookings.objects.filter(checkout_datetime__isnull=True)
        l = []
        for ele in data:
            Guest_object = Guest.objects.get(id=ele.Guest_id)
            room_object = Rooms.objects.get(id=ele.Room_id)
            l.append({'guest_id': Guest_object.id, 'room_id': room_object.id, 'name': Guest_object.firstName,
                      'roomName': room_object.room_number,
                      'people': ele.number_of_people, 'checkinTime': ele.checkin_datetime})

        d = {'info': l}
        return JsonResponse(d)


def roomAvailability(request):
    if request.method == "POST":
        room_size = request.POST.get("room_size")  # small
        room_type = request.POST.get('room_type')  # AC
        data = Rooms.objects.filter(reserved_room="No", room_size=room_size, room_type=room_type)
        l = []
        if data:
            for ele in data:
                l.append({"availableroom": ele.room_number})
        d = {'rooms': l}
        return JsonResponse(d)


def savebooking(guest_id, room_id, people, amount):
    # guest_id=request.POST.get("guest_id")
    # room_id=request.POST.get("room_id")
    # people=request.POST.get("people")
    # amount=request.POST.get("amount")
    data = Bookings(Guest_id=guest_id, Room_id=room_id, number_of_people=people, amount=amount)
    roomObject = Rooms.objects.get(id=room_id)
    roomObject.reserved_room = "Yes"
    data.save()
    roomObject.save()
    return "success"


@api_view(['GET', 'POST'])
def visitors(request):
    if request.method == "GET":
        snippets = Visitor.objects.all()
        serializer = VisitorSerializer(snippets, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        contact = request.POST.get('contact')
        room_number = request.POST.get('room_number')

        # Checking that the customer is available or not in Booking table
        roomList = Rooms.objects.filter(room_number=room_number)
        if roomList:
            roomObject  = roomList[0]
            room_id = roomObject.id
            if roomObject.reserved_room == "No":
                return Response("No customer in this room")
        else:
            return Response("No such room exist")

        #Checking if the visitor data is already available or not
        visitorcheck = Visitor.objects.filter(contact=contact)
        if visitorcheck:
            visitor_id = visitorcheck[0].id
            addvisitor_list(visitor_id,room_id)

        #saving data if customer is new
        serializer = VisitorSerializer(data=request.data)
        if serializer.is_valid():
            visitorObject = serializer.save()
            visitor_id = visitorObject.id
            addvisitor_list(visitor_id,room_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def addvisitor_list(visitor_id, room_id):
    visitorListObject = Visitor_list(Visitor_id=visitor_id,room_id=room_id)
    visitorListObject.save()




def liveVisitor(request):
    #taking out live visitor list
    data = Visitor_list.objects.filter(outDateTime__isnull=True)
    l=[]
    #Extracting each row data and appending them into the list
    for ele in data:
        l.append({'id':ele.id,'datetime':ele.inDateTime,'visitor_id':ele.Visitor_id,'room_id':ele.room_id})
    #converting list into dictionary so that we can send the same to the frontend as Json Response
    d={'visitor_list':l}
    return JsonResponse(d)


@api_view(['POST'])
def checkoutCustomer(request):
    if request.method == "POST":
        guest_id = request.POST.get('guest_id')
        room_id = request.POST.get('room_id')
        data = Bookings.objects.get(Guest_id=guest_id, Room_id=room_id)
        data.checkout_datetime = datetime.datetime.now()
        data.save()

        roomObject = Rooms.objects.get(id=room_id)
        roomObject.reserved_room = "No"
        roomObject.save()

        return Response('checked out successfully')


@api_view(['POST'])
def VisitorOut(request):
    if request.method == "POST":
        visitor_id = request.POST.get('visitor_id')
        visitorlistObject = Visitor_list.objects.get(Visitor_id=visitor_id, outDateTime__isnull=True)
        visitorlistObject.outDateTime = datetime.datetime.now()
        visitorlistObject.save()
        return Response("Visitor out successfully")


def date_wise_check(request):
    room_num=request.POST.get("room_num")
    date=request.POST.get("date")
    Bookings.objects.filter()
    

