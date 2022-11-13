from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from HotelApp.restviews import BookingsRestApi
from HotelApp.views import addGuest, liveVisitor, currentGuest, visitors, checkoutCustomer

router = routers.DefaultRouter()
router.register(r'bookings', BookingsRestApi)

urlpatterns = [
    path('bookings/',include(router.urls)),
    path('addGuest/',addGuest),
    path('livevisitor',liveVisitor),
    path('liveguest',currentGuest),
    path('visitors',visitors),
    path('checkout',checkoutCustomer),
    path('liveVisitor',liveVisitor)
]