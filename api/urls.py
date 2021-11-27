from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('arduino/', views.get_data_arduino, name='get_arduino_data'),
]