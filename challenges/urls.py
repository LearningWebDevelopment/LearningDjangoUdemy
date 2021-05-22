from django import views
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("jan", views.january),
    path("feb", views.february),
]
