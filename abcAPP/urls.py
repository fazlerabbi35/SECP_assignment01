from django.urls import path, include
from . import views

app_name = 'abcAPP'

urlpatterns = [
    path('', views.homepage, name='homepage')
]