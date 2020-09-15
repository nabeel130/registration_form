from django.shortcuts import render

from .forms import RegistrationForm

from .models import Jobform

# Create your views here.

def form_view(request):
    # form = Jobform.objects.all()
    # print(form)
    my_form = RegistrationForm()

    if request.method == "POST":
        my_form = RegistrationForm(request.POST)
        if my_form.is_valid():
            my_form.save()
            my_form = RegistrationForm()

    context = {
        "form" : my_form
    }

    
    return render(request, "reg_form.html", context)

def aboutUs(request):
    return render(request, "about.html")

def contactUs(request):
    return render(request, "contact.html")

def logIn(request):
    return render(request, "login.html")
        
    