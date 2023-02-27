from django.urls import path
from paginas.views import IndexView

urlpatterns = [
    path( 'inicio/', IndexView.as_view(), name='Inicio'),
]

