from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    if request.method == 'post':
        req = request.body.get('')
    print(req)
    return render(request, 'ki-tech/login.html', {"title" : "login"})

def home(request):
    return render(request, 'ki-tech/index.html', {"title" : "home"})

def about(request):
    return render(request, 'ki-tech/about.html', {"title" : "about"})

def service(request):
    return render(request, 'ki-tech/service.html', {"title" : "services"})

def contact(request):
    return render(request, 'ki-tech/contact.html', {"title" : "contact"})

def course(request):
    return render(request, 'ki-tech/course.html', {"title" : "courses"})