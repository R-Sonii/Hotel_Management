from rest_framework import viewsets

from HotelApp.models import Bookings, Visitor
from HotelApp.serializer import BookingsSerializer


class BookingsRestApi(viewsets.ModelViewSet):
    queryset = Bookings.objects.all()
    serializer_class = BookingsSerializer

