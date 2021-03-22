from django.urls import path
from . import views

app_name = 'receiving'
urlpatterns = [
    path('', views.applications_estado_r, name='receiving'),
    path('handin', views.applications_estado_o, name='handin'),
]