from django.urls import path, include
from . import views

urlpatterns = [
    # Paths del core
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('store/', views.store, name="store"),
]
