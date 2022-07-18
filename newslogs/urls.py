from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView , name="Home"),
    path('all/', views.newsView, name='All_News'),
    path('national/', views.newsView, name='National'),
    path('business/', views.newsView, name='Business'),
    path('sports/', views.newsView, name='Sports'),
    path('world/', views.newsView, name='World'),
    path('politics/', views.newsView, name='Politics'),
    path('technology/', views.newsView, name='Technology'),
    path('startup/', views.newsView, name='Startup'),
    path('entertainment/', views.newsView, name='Entertainment'),
    path('miscellaneous/', views.newsView, name='Miscellaneous'),
    path('hatke/', views.newsView, name='Unconventional'),
    path('science/', views.newsView, name='Science'),
    path('automobile/', views.newsView, name='Automobile'),
]
