from django.contrib import admin
from .models import Cidade
# Register your models here.

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display=('nome','sigla_estado',)
