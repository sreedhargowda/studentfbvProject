from django.shortcuts import render,redirect
from myApp.models import Student
from myApp.forms import StudentForm
# Create your views here.


def display(request):
    s=Student.objects.all()
    d={"stud":s}
    return render(request,'myApp/index.html',d)
