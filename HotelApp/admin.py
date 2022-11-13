from django.contrib import admin

from HotelApp.models import Guest, Rooms, Bookings, Employee, Department

admin.site.register(Guest)
admin.site.register(Rooms)
admin.site.register(Bookings)
admin.site.register(Department)

admin.site.register(Employee)
# Register your models here.
