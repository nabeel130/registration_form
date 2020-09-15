from django.db import models

# Create your models here.

DESIGNATION = (
    ('ACCOUNTS', 'ACCOUNTS'),
    ('IT' , 'IT'),
    ('SALES' , 'SALES'),
    ('CUSTOMER SERVICE' , 'CUSTOMER SERVICE'),
    ('DELIVERY SERVICE' , 'DELIVERY SERVICE')
)

GENDER = (
    ('male' , 'M'),
    ('female' , 'F'),
    ('other' , 'O')
)


class Jobform(models.Model):
    name = models.CharField(max_length = 256,default=None) 
    dob = models.DateField(max_length=12 , default=None)
    gender = models.CharField(
        choices=GENDER,
        default= 'GENDER',
        max_length=20
    )
    address1 = models.CharField(max_length = 256,default=None)
    pincode = models.CharField(max_length = 12,default=None)
    city = models.CharField(max_length = 256,default=None)
    country = models.CharField(max_length = 256,default=None)
    designation = models.CharField(
        choices = DESIGNATION,
        default = 'IT',
        max_length= 50
    )
    image = models.ImageField(blank = True , upload_to = 'profile/', null = True)
    vehicleregform = models.FileField(blank = True, upload_to='documents/')
    vehicleinsform = models.FileField(blank = True, upload_to='documents/')
    drivinglicenseform = models.FileField(blank = True, upload_to='documents/')
    aadharform = models.FileField(blank = True, upload_to='documents/')
    aadharno = models.IntegerField(default=None)
    drivingno = models.CharField(default=None,max_length=20)
    contactno1 = models.CharField(default=None,max_length=20)
    contactno2 = models.CharField(default=None,max_length=20)
    email = models.EmailField(max_length = 254)
    bankaccount = models.IntegerField(default=None)
    ifsc = models.CharField(max_length=50, blank=True, null=True)
    remarks =  models.BooleanField(default=True)
    