from django.urls import path
from . import views

app_name = 'Notas'

urlpatterns = [
    path('', views.IndexNotas, name='notas_index'),
    path('actualizar/<int:pk>', views.ConfimacionTarea, name='confimar_tarea'),
    path('nuevo/', views.AñadirTarea, name='nuevo')
]
