from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('relevance', views.relevance),
    path('geo', views.geo),
    path('skills', views.skills),
    path('recent', views.recent),
]
