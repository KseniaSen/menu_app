from django.http import HttpRequest, HttpResponse
from .templatetags.menu_tags import draw_menu


def menu_view(request: HttpRequest, menu_name: str) -> HttpResponse:
    """Функция для отображения меню."""

    menu_html = draw_menu(menu_name)

    return HttpResponse(menu_html)
