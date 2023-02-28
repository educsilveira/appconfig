""" Importar o TemplateView para criar páginas simples """
from django.views.generic import TemplateView

""" Create your views here. """
class IndexView(TemplateView):
    template_name = "index.html"

class PaginaInicial(TemplateView):
    template_name = "modelo.html"

class SobreView(TemplateView):
    template_name = "sobre.html"

class loginView(TemplateView):
    template_name = "login.html"    