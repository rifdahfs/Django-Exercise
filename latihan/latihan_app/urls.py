from django.urls import path
from latihan_app import views

urlpatterns = [
    path('', views.index, name='index'),
]