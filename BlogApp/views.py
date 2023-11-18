from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import *
# Create your views here.

def Home(request):
    allblogs = BlogModel.objects.all()
    lastblog = allblogs[len(allblogs)-1:][0]
    reverseblog = allblogs[::-1]
    recentfour = reverseblog[1:5]
    d = {"allblogs": allblogs, "lastblogs" : lastblog, "recentfour":recentfour}
    return render(request, 'index.html', d)

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')

def LoginForm(request):
    if request.method == "POST":
        d = request.POST
        u = d['username']
        p = d['pwd']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('User not found..')
    return render(request, 'login.html')

def Logoutuser(request):
    logout(request)
    return redirect('home')


def Signup(request):
    if request.method == "POST":
        d = request.POST
        u = d['username']
        p = d['pwd']
        f = d['fname']
        l = d['lname']
        e = d['email']
        a = d['about']
        img = request.FILES['profileimg']

        user = User.objects.create_user(username=u, password=p, first_name=f, last_name=l, email=e)
        UserDetail.objects.create(usr=user,userimage=img, aboutyou=a)
        return redirect('loginform')
    return render(request, 'signup.html')


def Blogdetail(request,bid):
    blog = BlogModel.objects.get(id = bid)
    userdetail = UserDetail.objects.get(usr = blog.usr)
    d = {"blog" : blog, "user":userdetail}
    return render(request, 'single.html', d)