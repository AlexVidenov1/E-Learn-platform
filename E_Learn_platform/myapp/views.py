
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from .forms import LoginForm, RegisterForm
from django.shortcuts import render, redirect
from .models import Course, Student, Teacher
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username, password=password)
            user.save()
            Student.objects.create(user=user)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(f"Logging in user: {user}")
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
        else:
            print("Form is not valid")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def student_courses_view(request):
    user = request.user
    try:
        student = user.student
        subscribed_courses = student.subscribed_courses.all()
    except Student.DoesNotExist:
        return redirect('home')
    context = {
        'courses': subscribed_courses
    }
    return render(request, 'student_courses.html', context)