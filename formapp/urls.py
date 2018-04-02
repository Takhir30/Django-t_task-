from django.urls import path

from . import views

urlpatterns = [
    path('', views.formapp, name='formapp'),
    path('inputs/', views.inputs, name='inputs'),
]
