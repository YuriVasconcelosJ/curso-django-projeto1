from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Sempre um método deve ter o argumento request
def home(request):
    return HttpResponse('Home 123')

def sobre(request):
    return HttpResponse('Sobre')

def contato(request):
    return HttpResponse('Contato')