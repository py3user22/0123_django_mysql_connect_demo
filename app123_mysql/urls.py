from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('home123_mysql_demo.html', views.home),
]