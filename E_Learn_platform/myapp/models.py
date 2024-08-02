from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Role(models.Model):
    STUDENT = 1
    TEACHER = 2
    ADMIN = 3
    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
        (ADMIN, 'Admin'),
    )
    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/', default='images/default.jpg')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    linkedin_account = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'Teacher: {self.user.email}'

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    enrollment_number = models.CharField(max_length=20, unique=True, default='0000000000')
    course = models.CharField(max_length=100, default='B.Tech')
    subscribed_courses = models.ManyToManyField('Course', related_name='students_subscribed')

    def __str__(self):
        return f'Student: {self.user.email}'

class Course(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    objectives = models.TextField(null=True, blank=True)
    owner = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    tags = models.CharField(max_length=200, default='')
    page_picture = models.ImageField(upload_to='images/', default='images/default.jpg')
    is_public = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)
    subscriptions = models.ManyToManyField(Student, blank=True, related_name='courses_subscribed')
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.title

class Section(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    description = models.TextField(blank=True, null=True)
    information = models.TextField(blank=True, null=True) # could be links, references, etc.

    def __str__(self):
        return self.title