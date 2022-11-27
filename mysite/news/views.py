from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Страница приложения news.")

def categories(request):
    return HttpResponse("Страница приложения categories.")

