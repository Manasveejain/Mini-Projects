from django.urls import path
from . import views
urlpatterns = [
    path('',views.home , name="home"),
    path('Dashboard/',views.dashboard , name="Dashboard"),
    path('Login/',views.login , name="login"),
]