from email.policy import default
from enum import unique
from django.db import models
from autoslug import AutoSlugField


# Create your models here.
class Contact(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=200)
    desc=models.CharField(max_length=500)
    address=models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=200,default="")
    slug=AutoSlugField(populate_from='title',unique=True,null=True,default=None)
    writer_img=models.ImageField(upload_to='image',default="")
    name=models.CharField(max_length=100,default="")
    image=models.ImageField(upload_to='image',default="")
    desc=models.TextField()
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name



class Departmentt(models.Model):
    name=models.CharField(max_length=100,default="")
    slug=AutoSlugField(populate_from='name',unique=True,null=True,default=None)
    image=models.ImageField(upload_to='image',default="")
    desc=models.TextField()

    def __str__(self):
        return self.name


class Team(models.Model):
    name=models.CharField(max_length=100,default="")
    speciality=models.CharField(max_length=100,default="")
    slug=AutoSlugField(populate_from='name',unique=True,null=True,default=None)
    image=models.ImageField(upload_to='image',default="")
    

    def __str__(self):
        return self.name


class Appointment(models.Model):
    name=models.CharField(max_length=100,default="")
    email=models.EmailField(blank=True,unique=False)
    phone=models.CharField(max_length=200)
    department=models.CharField(max_length=200)
    doctor_name=models.CharField(max_length=200)
    date=models.DateField(auto_now=False, auto_now_add=False)
    msg=models.CharField(max_length=500)
    
    def __str__(self):
        return self.name

class Carrier(models.Model):
    carrier=models.CharField(max_length=200)
    name=models.CharField(max_length=100,default="")
    email=models.EmailField(blank=True,unique=False)
    gender=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    
    address=models.CharField(max_length=200)
    exp=models.IntegerField()
    resume=models.FileField(upload_to='news',max_length=250,null=True,default=None)
    education=models.CharField(max_length=250)
    skill=models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
