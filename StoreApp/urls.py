from django.urls import path
from StoreApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produtos/', views.produtos_lista, name='produtos_lista'),
    path('produto/', views.produto_detalhe, name='produto_detalhe')
]