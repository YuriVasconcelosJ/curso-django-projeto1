# Impotação que serve para ler um arquivo e renderizar ele
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Sempre um método deve ter o argumento request
def home(request):
    return render(request, 'home.html')

def sobre(request):
    return HttpResponse('Sobre')

def contato(request):
    return HttpResponse('Contato')