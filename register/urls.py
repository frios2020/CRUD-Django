from django.urls import path

from . import views
app_name = 'register'
urlpatterns = [
    path('', views.ApplicationsListToday, name='applications-today'),
    path('Applications-Create', views.ApplicationsCreate, name='applications-create'),
    path('Applications-Update/<int:id>', views.ApplicationsUpdate, name='applications-update'),
    path('Applications-Delete/<int:id>', views.ApplicationsDelete, name='applications-delete'),
]