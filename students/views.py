from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def students(request):
    student=[{
        'name':'Aditya',
        'age':25
    }]
    return HttpResponse(student)
