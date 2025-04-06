from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_processo, name='cadastrar_processo'),
    path('compromissos/cadastrar/', views.cadastrar_compromisso, name='cadastrar_compromisso'),
]
