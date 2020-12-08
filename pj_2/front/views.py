from django.shortcuts import render


def index(request):
    return render(request, 'front/index.html')


def about(request):
    return render(request, 'front/about.html')


def algem(request):
    return render(request, 'front/algem.html')
