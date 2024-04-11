from django.urls import path
from StoreApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produtos/', views.produtos_lista, name='produtos_lista'),
    path('produtos/<int:id>', views.produtos_lista_por_departamento, name='produtos_lista_por_departamento'),
    path('produto/<int:id>', views.produto_detalhe, name='produto_detalhe')
    
]
    