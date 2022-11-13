from HotelApp.models import Bookings, Visitor
from rest_framework import  serializers

class BookingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Bookings
        fields=['Guest_id','Room_id','number_of_people','checkin_datetime','checkout_datetime','amount']

class VisitorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Visitor
        fields = ['firstName','lastName','contact','email','idtype','idnumber','address','city','state']