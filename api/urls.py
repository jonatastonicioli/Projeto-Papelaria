from django.urls import path
from .views import listar_categorias

urlpatterns = {
    path('categorias', listar_categorias)

    



    
}