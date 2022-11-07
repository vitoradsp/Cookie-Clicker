from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.index, name='index'),
    path('login/', views.logar, name='logar'),
    path('logout/', views.deslogar, name='saiporra'),
]