from django.urls import path

from . import views

app_name = 'pokedex'

urlpatterns = [
    path('', views.index, name='index'),
    path('pokemon/<int:pokemon_id>/', views.pokemon, name='pokemon'),
    path('pokemon/add/', views.add_pokemon, name='add_pokemon'),
    path('pokemon/edit/<int:pk>/', views.edit_pokemon, name='edit_pokemon'),
    path('pokemon/delete/<int:pk>/', views.delete_pokemon, name='delete_pokemon'),
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('trainers/', views.trainer, name='trainers'),
    path('trainers/add/', views.add_trainer, name='add_trainer'),
    path('trainers/edit/<int:pk>/', views.edit_trainer, name='edit_trainer'),
    path('trainers/delete/<int:pk>/', views.delete_trainer, name='delete_trainer'),
    path('logout/', views.logout_view, name='logout'),
]