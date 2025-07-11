from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.index, name="Hello genio_ml"),
    path('get_data/', views.get_data, name="Get data genio_ml"),
    path('random/', views.random_number, name="Random number genio_ml"),
]