from django.shortcuts import render
from .models import LearningResource, LearningPath, LearningPathItem

def home(request):
    return render(request, "home.html")
  
def path_list(request):
    paths= LearningPath.objects.all().order_by("name")
    content={
        "paths" : paths
    }
    return render(request,"path_list.html", content)
    
def resources(request):
    resources = LearningResource.objects.all()
    content={
        "resources" : resources
    }
    return render(request,"resources.html", content)
    
def path_detail (request, id):
    path = LearningPath.objects.get(id=id )
    items = LearningPathItem.objects.filter(path = path).order_by("order")
    content={
        "path":path,
        "items":items
    }
    return render(request,"path_detail.html", content) 

def dashboard(request):
    return render(request, "dashboard.html")

def login(request):
    return render(request, "login.html")