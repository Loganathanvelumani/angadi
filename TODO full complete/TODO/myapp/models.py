from django.db import models

# Create your models here.
class work(models.Model):
    Tittel=models.CharField(max_length=35)
    Description=models.CharField(max_length=200)

class Register(models.Model):
    Name=models.CharField(max_length=30)
    Password=models.CharField(max_length=16)
    Conpass=models.CharField(max_length=16)

class complete(models.Model):
    Done=models.CharField(max_length=40)
