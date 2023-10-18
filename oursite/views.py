from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'Home.html')

def navbar(request):
    return render(request,'nav.html')

def footer(request):
    return render(request,'footer.html')