from typing import List
from django import template
from django.utils.safestring import mark_safe
from ..models import MenuItem


register = template.Library()


@register.simple_tag
def draw_menu(menu_name: str) -> str:
    """Функция для отображения меню с указанным именем"""
    menu_items = MenuItem.objects.filter(title=menu_name).select_related('parent')
    return mark_safe(render_menu_item(menu_items))


def render_menu_item(menu_items: List[MenuItem]) -> str:
    """Рекурсивная функция для отображения элементов меню и их дочерних элементов."""
    menu_html = '<ul>'
    for item in menu_items:
        menu_html += '<li>'
        if item.url:
            menu_html += f'<a href="{item.url}">{item.title}</a>'
        elif item.named_url:
            menu_html += f'<a href="{item.named_url}">{item.title}</a>'
        else:
            menu_html += item.title
        if item.children.exists():
            menu_html += render_menu_item(item.children.all())
        menu_html += '</li>'
    menu_html += '</ul>'
    return menu_html
