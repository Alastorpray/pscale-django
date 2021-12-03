from django.contrib import admin
from .models import Categorias, Estado, Zona, Clientes


# Register your models here.

class categoriasadmin(admin.ModelAdmin):
    list_display = ['idcategorias', 'descripcion']
    ordering = ['idcategorias']

class estadoadmin(admin.ModelAdmin):
    list_display = ['idestado', 'descripcion']
    ordering = ['idestado']

class zonaadmin(admin.ModelAdmin):
    list_display = ['idzona', 'nombre']
    ordering = ['idzona']

class clientesadmin(admin.ModelAdmin):
    list_display = ['idclientes', 'nombres', 'apellidos', 'direccion', 'telefono', 'idcategorias', 'idzona', 'comentario', 'idestado']
    ordering = ['idclientes']




admin.site.register(Categorias, categoriasadmin)
admin.site.register(Estado, estadoadmin)
admin.site.register(Zona, zonaadmin)
admin.site.register(Clientes, clientesadmin)