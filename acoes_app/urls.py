from django.urls import path
from .views import acoes_view

urlpatterns = [
    path('', acoes_view, name='acoes'),  # Página principal
]