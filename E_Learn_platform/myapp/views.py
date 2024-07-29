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

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Redirect to home page after successful registration
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})