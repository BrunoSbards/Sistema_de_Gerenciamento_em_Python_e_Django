from django.contrib import admin
from django.urls import path, include
from .views import home, salvar, editar, update, delete, alterar, logout
from . import views

urlpatterns = [    
    path('', home),
    path('salvar/', salvar, name="salvar"),
    path('editar/<int:id>/', editar, name="editar"),
    path('update/<int:id>/', update, name="update"),
    path('delete/<int:id>/', delete, name="delete"),
    path('cadastro/', views.cadastro, name="cadastro"),   
    path('login/', views.login, name="login"),
    path('plataforma/', views.plataforma, name="plataforma"),
    path('plataforma/alterar/', alterar, name="alterar"),
    path('logout', logout, name="logout")    
]