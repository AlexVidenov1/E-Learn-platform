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

    def __str__(self):
        return f'Student: {self.user.email}'
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_public = models.BooleanField(default=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title