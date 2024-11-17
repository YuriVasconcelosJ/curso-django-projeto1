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