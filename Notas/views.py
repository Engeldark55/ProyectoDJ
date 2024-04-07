from django.shortcuts import render

# Create your views here.
def IndexNotas(req):
    context = {
        'titulo': 'Recordatorios.',
        'estado': 'active'
    }
    return render(req, 'Notas/index.html', context)