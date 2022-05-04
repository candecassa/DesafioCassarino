from django.db import models

# Create your models here.
class Familiar1(models.Model):
    nombre= models.CharField(max_length=50)
    edad= models.IntegerField()
    email= models.EmailField()
    

class Familiar2(models.Model):
    nombre= models.CharField(max_length=50)
    edad= models.IntegerField()
    email= models.EmailField()
    
    

class Familiar3(models.Model):
    nombre= models.CharField(max_length=50)
    edad= models.IntegerField()
    email= models.EmailField()
    