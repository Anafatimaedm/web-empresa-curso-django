from urllib import request
from .models import Link

# ctx contexto  dict diccionario diccionario de contexto
# Esto fue para hacer la prueba
# def ctx_dict(request):
#     ctx = {'test':'hola'}
#     return ctx  

def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] =link.url
    return ctx