from django.urls import path
from . import views
urlpatterns = [
    path('', views.IndexNotas, name='notas_index')
]
