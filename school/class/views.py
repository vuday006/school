from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Student, Teacher


def home(request):
    return render(request, 'home.html')


"""to authticate user login"""


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.student.is_teacher:
                return HttpResponseRedirect(reverse('student_details'))
            elif user.teacher:
                return HttpResponseRedirect(reverse('teacher_details'))
            else:
                return HttpResponseRedirect(reverse('student_details'))
        else:
            return render(request, "teacher/login.html")
    else:
        if request.user.is_authenticated:
            student = Student.objects.all()
            return render(request, "student_details.html", {"student": student})
        return render(request, "login.html")


""""view to get teacher details"""


def teacher_details(request):
    teacher = Teacher.objects.all()
    return render(request, 'teacher_details.html', {'Teacher': teacher})


""""view to gettudent details"""


def student_details(request):
    student = Student.objects.all()
    return render(request, 'student_details.html', {'student': student})
