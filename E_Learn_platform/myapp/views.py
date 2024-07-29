
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from django.shortcuts import render, redirect
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


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            user_type = form.cleaned_data.get('user_type')
            if user_type == 'student':
                Student.objects.create(user=user)
            else:
                Teacher.objects.create(user=user)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})