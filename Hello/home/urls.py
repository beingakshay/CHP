from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about.html/", views.about, name='about'),
    path("services.html/", views.services, name='services'),
    path("/contact.html/", views.contact, name='contact'), 
]
