# Impotação que serve para ler um arquivo e renderizar ele
from django.shortcuts import render
# Create your views here.

# Sempre um método deve ter o argumento request
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Yuri Vasconcelos'
    })
