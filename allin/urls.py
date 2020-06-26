from django.urls import path
from .import views

app_name = 'allin'

urlpatterns = [
    path('', views.home),
    path('articles', views.articles, name='articles'),
    path('second', views.god, name='god'),
]
