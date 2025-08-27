from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id=models.CharField(max_length=21)
    name=models.CharField(max_length=51)
    designation=models.CharField(max_length=21)

    def __str__(self):
        return self.name
