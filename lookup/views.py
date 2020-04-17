from django.shortcuts import render

# Create your views here.

def home(request): #home corresponds with the home.html file
	return render(request, "home.html", {}) # here we return the request and thge address (home.html), and a dictionnary

def about(request): #home corresponds with the home.html file
	return render(request, "about.html", {})