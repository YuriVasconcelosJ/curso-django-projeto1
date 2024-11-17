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

# urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('', my_view) <- Representação da raiz de um site/ página inicial
# ]
- **Métodos de requisição:**
 `GET(Solicita um recurso específico.), POST(Envia dados para o servidor para criar ou processar algo.), PUT(Atualiza completamente um recurso.), DELETE(Deleta algum recurso do servidor)`
--------------------------------------------------------
## urls.py

# Entender mais sobre esse startapp e a questão das urls(Ainda não entendi como é feito essa substituição dos dois).

- **Organização:**
  `Por questão de organização de projeto podemos dividir ele em apps por meio do comando: python manager.py statapp <nome do parte a ser dividida de sua aplicação>`

  `Nela podemos mover a questão de urls e views.`

**Antiga forma de organização de urls:**
# from recipes.views import home, sobre, contato
# urlpatterns = [
#   path('admin/', admin.site.urls),
#   path('', home),
#   path('sobre/', sobre),
#   path('contato/', contato),
# ]

**Nova forma de organização:**

`Criando um arquivo urls.py na pasta de apps`

# from django.urls import path
# from recipes.views import home, sobre, contato

# urlpatterns = [
#   path('', home),
#   path('sobre/', sobre),
#   path('contato/', contato),
# ] 
