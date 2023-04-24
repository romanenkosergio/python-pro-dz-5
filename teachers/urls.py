from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("all_teachers", views.get_teachers_list, name="get_teachers_list"),
]
