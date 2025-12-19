from django.urls import path
from . import views
urlpatterns = [
    path('',views.home , name="home"),
    path('path/',views.path_list, name="path" ),
    path('path/<int:id>/',views.path_detail, name="path-id" ),
    path('resources/',views.resources, name="resources" ),
    # path('Dashboard/',views.dashboard , name="Dashboard"),
    # path('Login/',views.login , name="login"),
]