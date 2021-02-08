from django.urls import path
from . import views

urlpatterns = [
    path('arquivos/', views.arquivos, name='arquivos'),
    path('processos/', views.processos, name='processos'),
    path('processos/<int:pid>', views.detalhar, name='processo'),
]