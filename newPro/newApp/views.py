from django.shortcuts import render

# # Генерация стандартного HTTP ответа 
# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello, World!")

# # Create your views here.

from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    print(request.__dict__)
    return render(request, 'newApp/index.html')

# Новая страница About
def about(request):
    # print(request.__dict__)
    return render(request, 'newApp/about.html')