from django.shortcuts import render
from django.http import HttpResponse


def index(request):  #создали функцию, которая будет работать при переходе на главную стр
    return render(request, 'main/index.html') #render - метод для шаблона httpresponse


def about(request):
    return render(request, 'main/about.html')