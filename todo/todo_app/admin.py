from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Todo
@admin.register(Todo)
class TodoAdmin(ModelAdmin):
    search_fields = ['id', 'nom', 'batafsil']
    list_filter = ['batafsil','status']
    ordering = ['vaqt']
    list_display = ['nom','batafsil','vaqt']
