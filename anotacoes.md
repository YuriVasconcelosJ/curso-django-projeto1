# Minhas Anotações
## Aula de Django
- **Comando para criar um projeto Django:**  
  `django-admin startproject <nome do projeto> .`
- **Rodar o projeto:**  
  `python manage.py runserver`
- **Comando para criar o ambiente virtual:** 
  `python -m venv <nome da pasta>`
- **Comando para parar a execução do ambiente virtual:**
  `deactivate`
--------------------------------------------------------

## Conhecimento HTTP

~~~python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_view) <- Representação da raiz de um site/página inicial
 ] 
~~~

- **Métodos de requisição:**
   GET(Solicita um recurso específico.), 
   POST(Envia dados para o servidor para criar ou processar algo.), 
   PUT(Atualiza completamente um recurso.), 
   DELETE(Deleta algum recurso do servidor)
--------------------------------------------------------
## urls.py

- **Organização:**
  `Por questão de organização de projeto podemos dividir ele em apps por meio do comando: python manager.py statapp <nome do parte a ser dividida de sua aplicação>`

  `Nela podemos mover a questão de urls e views.`

**Antiga forma de organização de urls:**
~~~python
 from recipes.views import home, sobre, contato
 urlpatterns = [
   path('admin/', admin.site.urls),
   path('', home),
   path('sobre/', sobre),
   path('contato/', contato),
 ]
~~~

**Nova forma de organização:**

`Criando um arquivo urls.py na pasta de apps`

~~~python
 from django.urls import path
 from recipes.views import home, sobre, contato

 urlpatterns = [
   path('', home),
   path('sobre/', sobre),
   path('contato/', contato),
 ] 
~~~
---
## Templates e renderização de HTML no Django

`from django.shortcuts import render`
**Essa importação faz com que a gente tenha a capacidade de criar templates e o django vai ler e renderizar**
**Utilizamos ele para fazer o chamado do template(no diretório template) para a pasta de views**

**Utilização do render para fazer o chamado do template**
~~~python
def home(request):
    return render(request, 'home.html')
~~~

**Devemos declarar o app que a gente criou em nosso projeto no arquivo settings.py**

---
## NameSpaces

Continuar dps
**Usado para evitar conflitos em diretórios, arquivos estáticos, urls**

## Arquivos Estáticos

Os arquivos estáticos em Django são recursos que não mudam com frequência e são usados para estilizar e melhorar a interação do site. Eles incluem CSS, JavaScript, imagens, fontes e outros arquivos relacionados.