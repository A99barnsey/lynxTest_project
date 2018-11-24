from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Course
from django.contrib.auth import authenticate
from django.contrib.auth.models import User 

# Create your views here.


# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         redirect('dashboard')
#     else:
#         redirect('login')

def dashboard(request):
    courses = Course.objects.all().filter(teacher=request.user.id)
    context = {
        'courses':courses,
    }
    return render(request, 'accounts/dashboard.html', context)


def course(request, course_id):
    return HttpResponse('<h1>Course page for course id {{course_id}}</h1>')

def courses(request):
    return redirect('dashboard')