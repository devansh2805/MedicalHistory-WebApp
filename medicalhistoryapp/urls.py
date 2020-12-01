from django.urls import path, include, re_path
from . import views # . signifies current Package


urlpatterns = [
    path('', views.homePage, name='home'),
]