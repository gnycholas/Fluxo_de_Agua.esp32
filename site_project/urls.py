from django.urls import path
from . import views

app_name = 'site_project'

urlpatterns = [
    path('', views.index, name='index'),
]