from django.contrib import admin
from .models import Emprendedor, Emprendimiento, Cliente, Administrador

# Register your models here.

admin.site.register(Emprendedor)
admin.site.register(Emprendimiento)
admin.site.register(Cliente)
admin.site.register(Administrador)
