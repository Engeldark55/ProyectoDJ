from django.shortcuts import render, redirect
from .models import Tarea
from datetime import datetime
from .forms import TareaForm

# Create your views here.
def IndexNotas(req):
    ListadoTareas = Tarea.objects.filter(estado = 'not ok')
    context = {
        'titulo': 'Recordatorios.',
        'estado': 'active',
        'formulario': '',
        'lista': ListadoTareas,   
        'fecha': datetime.now
    }
    return render(req, 'Notas/index.html', context)

def ConfimacionTarea(request, pk):
    ListadoTarea = Tarea.objects.get(pk=pk)
    if request.method == 'POST':
        ListadoTarea.delete()
    return redirect('Notas:notas_index')

def AñadirTarea(req):
    NuevoForm = TareaForm
    context = {
        'titulo': 'Recordatorios.',
        'form':NuevoForm
    }
    return render(req, 'Notas/components/añadir.html', context)