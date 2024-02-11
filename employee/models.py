from django.db import models

# Create your models here.


class Employee(models.Model):
    name=models.CharField(max_length=100,blank=False)
    position=models.CharField(max_length=100,blank=False)
    department=models.CharField(max_length=100,blank=False)

    def __str__(self):
        return self.name
   