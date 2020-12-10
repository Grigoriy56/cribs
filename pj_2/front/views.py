from django.shortcuts import render
from .models import Thems


def index(request):
    results = Thems.objects.all()
    return render(request, 'front/index.html', {'thems': results})


def about(request):
    return render(request, 'front/about.html')


def algem(request):
    return render(request, 'front/algem.html')


def matrix(request):
    return render(request, 'front/matrix.html')


def matrix_a(request):
    return render(request, 'front/matrix_addition.html')


def matrix_mult(request):
    return render(request, 'front/matrix_multiplication.html')


def matrix_mult1(request):
    return render(request, 'front/matrix_multiplication_na_chyslo.html')


def matrix_tr(request):
    return render(request, 'front/matrix_transpose.html')
