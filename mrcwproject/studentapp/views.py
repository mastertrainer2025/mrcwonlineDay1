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
