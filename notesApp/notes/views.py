from django.shortcuts import render, redirect,get_object_or_404
from .models import Note
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from django.contrib import messages

def register_user(request):
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username= username).exists():
            messages.error(request, "Username already taken")
            return redirect('register')
        
        user = User.objects.create_user(username = username, email= email, password = password)
        user.save()
        
        login(request,user)
        return redirect('home')
    return render(request,'register.html')

@login_required
def home(request):
    notes =Note.objects.filter(user =request.user)
    return render(request, 'home.html', {"notes" : notes})

@login_required
def add_note(request):
    if request.method =="POST":
        title = request.POST['title']
        content = request.POST['content']
        Note.objects.create(title = title, content = content, user= request.user)
        return redirect('home')
    return render(request, 'add_note.html')

@login_required
def edit_note(request, id):
    note = get_object_or_404(Note , id=id)
    if request.method == "POST":
        note.title = request.POST['title']
        note.content = request.POST['content']
        note.save()
        return redirect('home')
    return render(request, 'edit_note.html', {"note": note})
 
@login_required   
def delete_note(request, id):
    note = get_object_or_404(Note , id=id )
    note.delete()
    return redirect('home')


