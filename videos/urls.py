from django.urls import path

from . import views

urlpatterns = [
    path('discover/', views.discover, name='discover'),
    path('generate/', views.generate, name='generate'),
]
