from django.contrib import admin
from django.contrib.auth.models import Group

from .models import (Ingredient)

admin.site.unregister(Group)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """Настройка Ingredient для панели Admin"""

    list_display = ('pk', 'name', 'measurement_unit')
    list_filter = ('name',)
    search_fields = ('name',)
    list_editable = ('name', 'measurement_unit',)
