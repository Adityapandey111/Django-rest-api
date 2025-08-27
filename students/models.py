from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=51)
    student_id=models.CharField(max_length=11)
    branch=models.CharField(max_length=21)

    def __str__(self):
        return self.name
    
