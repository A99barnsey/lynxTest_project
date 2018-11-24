from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class Course(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

class Student(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.IntegerField()
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30)
    id_number = models.IntegerField(unique=True, blank=True)



