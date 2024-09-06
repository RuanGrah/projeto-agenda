from django.contrib import admin

from django.contrib.admin import AdminSite

from .models import Categoria, Contato
# Register your models here.
class Contato_admin(admin.ModelAdmin):
    list_display = ("nome", "telefone" ,"data_nascimento",  "email")

admin.site.register(Categoria)
admin.site.register(Contato,Contato_admin)

# Mudanças Visuais

admin.site.site_header = "Agenda Pessoal"
admin.site.site_title = "Site Agenda"
admin.site.index_title = "Bem-vindo a sua Agenda Pessoal"



