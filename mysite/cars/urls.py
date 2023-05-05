from django.contrib import admin
from django.urls import path, include
from .views import *

from django.views.decorators.cache import cache_page

app_name = 'car'
urlpatterns = [
    path('car/create/', CarCreateView.as_view()),
    path('all/', cache_page(60)(CarsListView.as_view())),
    path('car/detail/<int:pk>/', CarsDetailView.as_view())
]
