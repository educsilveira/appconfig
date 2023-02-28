from django.urls import path
from paginas.views import IndexView,PaginaInicial,SobreView, loginView

urlpatterns = [
    path( '', IndexView.as_view(), name='Home'),
    path( '', PaginaInicial.as_view(), name='conteudo'),
    path( '', SobreView.as_view(), name='sobre'),
    path( '', loginView.as_view(), name='login'),
]

