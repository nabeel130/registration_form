from django import forms

from .models import Jobform


YEARS= [x for x in range(1980,2011)]

class RegistrationForm(forms.ModelForm):
    name = forms.CharField(label = 'NAME' , widget= forms.TextInput (attrs= { "placeholder" : "your name"}))
    dob = forms.CharField(label='D.O.B' , widget=forms.SelectDateWidget(years=YEARS ,attrs={'class' :"dateofbirth"}))
    GENDER = (
    ('male' , 'M'),
    ('female' , 'F'),
    ('other' , 'O')
)
    gender = forms.ChoiceField(choices=GENDER)
    address = forms.CharField(
        label = 'ADDRESS',
        widget= forms.Textarea(
            attrs= {
                "placeholder" : "your address",
                "rows" : 5,
                "cols" : 30,
                'class' :"address-name"
            })
        )
    pincode = forms.CharField(label= "PINCODE")
    city = forms.CharField(label="CITY" , widget= forms.TextInput( attrs= {"placeholder" : "your city", 'class' :"city-name"}))
    country = forms.CharField(label="COUNTRY" , widget= forms.TextInput( attrs= {"placeholder" : "your country", 'class' :"country-name"}))
    image = forms.ImageField(label= "select an image")
    vehicleregform = forms.FileField(label="Vehicle Reg.Form")
    vehicleinsform = forms.FileField(label="Vehicle Insurance")
    drivinglicenseform = forms.FileField(label="DRIVING LICENSE")
    aadharform= forms.FileField(label="Aadhar form")
    DESIGNATION = (
    ('ACCOUNTS', 'ACCOUNTS'),
    ('IT' , 'IT'),
    ('SALES' , 'SALES'),
    ('CUSTOMER SERVICE' , 'CUSTOMER SERVICE'),
    ('DELIVERY SERVICE' , 'DELIVERY SERVICE')
 )
    designation = forms.ChoiceField(choices=DESIGNATION)
    aadharno = forms.IntegerField(label= "AADHAR CARD NO " , widget= forms.TextInput (attrs= {"placeholder" : "your addhar number", 'class' :"aadharno"}))
    drivingno = forms.IntegerField(label= "DRIVING LICENSE NO" , widget=forms.TextInput(attrs= {"placeholder" : "licese no", 'class' :"licenseno"}))
    contactno1 = forms.CharField(label= 'CONTACT NUMBER 1' , widget=forms.NumberInput(attrs= {"placeholder" : "your number", 'class' :"contact1"}))
    contactno2 = forms.CharField(label= 'CONTACT NUMBER 2', widget=forms.NumberInput(attrs= {"placeholder" : "your number", 'class' :"contact2"}))
    email =  forms.EmailField(label="EMAIL ID" , widget= forms.EmailInput(attrs={"placeholder" : "your mail id", 'class' :"email-id"}))
    bankaccount = forms.IntegerField(label='BANK ACCOUNT NO', widget=forms.NumberInput(attrs= {"placeholder" : "your number", 'class' :"bankaccount"}))
    ifsc = forms.CharField(label="IFSC NUMBER")
    remarks = forms.BooleanField()



    class Meta :
        model = Jobform
        fields = [
            'name',
            'dob',
            'gender',
            'address',
            'pincode',
            'city',
            'country',
            'designation',
            'aadharno',
            'drivingno',
            'contactno1',
            'contactno2',
            'email',
            'bankaccount',
            'ifsc',
            'image',
            'vehicleregform',
            'vehicleinsform',
            'drivinglicenseform',
            'aadharform'
            
        ]

        