import imp
from django.urls import path, include
from . import views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative'),
    path('base/', views.base, name='base')

]