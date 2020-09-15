from .views import form_view , aboutUs , contactUs , logIn

from django.urls import path

urlpatterns = [
    path('' , form_view , name = "form_view"),
    path('about/' , aboutUs , name = "aboutus"),
    path('contact/' , contactUs , name = "contactus"),
    path('login/' , logIn , name = "login")
    
]