# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return render(request, 'pages/about.html')


def rules(request):
    return render(request, 'pages/rules.html')
