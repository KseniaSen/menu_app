from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class ProductAdmin(admin.ModelAdmin):
    """Настройки панели администратора для модели MenuItem."""

    list_display = ['pk', 'title', 'url', 'named_url', 'parent']
    list_display_links = ['pk', 'title']
    list_filter = ('title', 'named_url')
    search_fields = ['title', 'parent', 'url', 'named_url']
    ordering = ['pk']
