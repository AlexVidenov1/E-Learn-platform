from django.shortcuts import render
from .models import Student, Teacher

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def student(request):
    students = Student.objects.all()
    return render(request, 'student.html', {'students': students})

def teacher(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher.html', {'teachers': teachers})