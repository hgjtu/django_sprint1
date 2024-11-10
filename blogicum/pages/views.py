from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def about(request):
    return HttpResponse('Страничка about')


def rules(request):
    return HttpResponse('Страничка rules')
