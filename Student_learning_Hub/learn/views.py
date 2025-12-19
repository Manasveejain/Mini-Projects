from django.shortcuts import render
from django.http import  HttpResponse


def home(request):
    return render(request, "home.html")
  
def path_list(request):
    pass
def resources(request):
    pass
def path_detail (request, id):
    pass  

def dashboard(request):
    return render(request, "dashboard.html")

def login(request):
    return render(request, "login.html")