from django.conf.urls import url
from django.urls import path
from appTwo import views

urlpatterns = [
    path('', views.help, name='help'),
    path('help/', views.help, name='help'),
]
