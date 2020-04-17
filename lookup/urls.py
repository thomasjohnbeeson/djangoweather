from django.contrib import admin
from django.urls import path
from lookup import views

urlpatterns = [ #here are all the listed urls used in the app
	path('', views.home, name = "home"), #the first '' are the address in the url, since this is home, it's blank
    path('about.html', views.about, name = "about"), #the name is used for referemce in embedded python code in html files

]