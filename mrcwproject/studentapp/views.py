from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("Hello, World!")

def morning(request):
    return HttpResponse("Good Morning, World!")

def evening(request):
    return HttpResponse("Good Evening, World!")

def night(request):
    return HttpResponse("Good Night, World!")
    
def html(request):
    return render(request, 'index.html')
def registration(request):
    return render(request, 'registration.html')
def login(request):
    return render(request, 'login.html')
def dashboard(request):
    return render(request, 'dashboard.html')
def profile(request):
    return render(request, 'profile.html')
def contact(request):
    return render(request, 'contact.html')