from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Guest(models.Model):
    # id = 1,2,3,4,5
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    idtype = models.CharField(max_length=50)
    idnumber = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.firstName


class Rooms(models.Model):
    id = models.AutoField(primary_key=True)
    room_number = models.CharField(max_length=50)
    room_size = models.CharField(max_length=50)  # small,medium,large
    room_type = models.CharField(max_length=50)  # AC/Non-AC
    room_price = models.CharField(max_length=50)
    reserved_room = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Rooms"

    def __str__(self):
        return self.room_number


class Bookings(models.Model):
    # id = models.AutoField(primary_key=True)
    Guest = models.ForeignKey(Guest, on_delete=models.DO_NOTHING)  # 4 Guest_id
    Room = models.ForeignKey(Rooms, on_delete=models.DO_NOTHING)
    number_of_people = models.CharField(max_length=10)
    checkin_datetime = models.DateTimeField(auto_now_add=True)
    checkout_datetime = models.DateTimeField(null=True)
    # emp_id=models.CharField(max_length=50)
    amount = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Bookings"

    def __str__(self):
        return str(self.id)


class Visitor(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    contact = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    idtype = models.CharField(max_length=50)
    idnumber = models.CharField(max_length=50,unique=True)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)


    def __str__(self):
        return self.firstName

class Visitor_list(models.Model):
    Visitor = models.ForeignKey(Visitor,on_delete=models.DO_NOTHING)
    room = models.ForeignKey(Rooms,on_delete=models.DO_NOTHING)
    inDateTime = models.DateTimeField(auto_now_add=True)
    outDateTime = models.DateTimeField(null=True)


class Department(models.Model):
    dept_name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.dept_name

class Employee(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    contact = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    idtype = models.CharField(max_length=50)
    idnumber = models.CharField(max_length=50,unique=True)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    salary= models.CharField(max_length=10)
    account_number = models.CharField(max_length=20)
    dept = models.ForeignKey(Department,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.firstName + " " + self.lastName