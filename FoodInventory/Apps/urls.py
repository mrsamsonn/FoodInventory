from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index, name='index'),
    # path('process-input/', views.process_input, name='process_input'),
]