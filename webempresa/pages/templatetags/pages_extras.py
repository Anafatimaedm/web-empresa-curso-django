from django import template
from pages.models import Page
# Para registrarlo en la libreria de templates
register = template.Library()
# Es un decorador que va a implementar la funcionalidad
@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages