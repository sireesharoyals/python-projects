from django.db import models

# Create your models here.

class student(models.Model):

    name = models.CharField(max_length=1000)
    classname = models.CharField(max_length=1000)
    fathername = models.CharField(max_length=1000)
    contact = models.IntegerField(max_length=10)

