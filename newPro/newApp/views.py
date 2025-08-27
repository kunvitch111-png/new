from django.shortcuts import render

# # Генерация стандартного HTTP ответа 
# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello, World!")

# # Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")