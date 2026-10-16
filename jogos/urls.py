from django.urls import path
from . import views

app_name = 'jogos'

urlpatterns = [
    path('', views.index, name='index'),
    path('equipes/<int:equipe_id>/', views.equipe, name='equipe'),
    path('modalidades/<int:modalidade_id>/', views.modalidade, name='modalidade'),
]