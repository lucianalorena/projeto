from django.contrib import admin

#Registrar um modelo no painel de administração do Django
#O que é o painel de administração:  é uma interface pré-construída fornecida pelo Django que permite aos administradores do sistema gerenciar os dados do aplicativo sem a necessidade de escrever código personalizado para interfaces administrativas
from .models import Task, Musician 
admin.site.register(Task)
admin.site.register(Musician)