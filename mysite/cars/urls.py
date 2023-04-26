from django.contrib import admin
from django.urls import path, include
from .views import *
app_name = 'car'
urlpatterns = [
    path('car/create/', CarCreateView.as_view()),
    path('all/', CarsListView.as_view()),
    path('car/detail/<int:pk>/', CarsDetailView.as_view())

]
