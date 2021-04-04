from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Student(models.Model):
    Gender_choices = (
        ("MALE", 'male'),
        ('FEMALE', 'female')
    )
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(max_length=30)
    gender = models.CharField(max_length=100, choices=Gender_choices)
    address = models.CharField(max_length=100)
    father_mobile_number = models.CharField(max_length=20)
    is_student = models.BooleanField(default=False)

    def __str__(self):
        return self.name.username


class Teacher(models.Model):
    Gender_choices = (
        ("MALE", 'male'),
        ('FEMALE', 'female')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(max_length=30)
    gender = models.CharField(max_length=30, choices=Gender_choices)
    address = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    experience = models.CharField(max_length=50)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username