from django.db import models

# Create your models here.
class Tarea(models.Model):
    ESTADO_CHOICES = [
                        ('ok', True),
                        ('not ok', False) 
                    ]
    nombre = models.CharField(verbose_name="nombre  de la tarea: ", max_length=50)
    descripcion = models.TextField(verbose_name="sobre que trata...")
    estado = models.CharField(verbose_name= 'Estado: ',choices=ESTADO_CHOICES, max_length=50, default="not ok")
    creado = models.DateTimeField(verbose_name='creado el dia: ', auto_now=False, auto_now_add=True)
    class Meta:
        verbose_name = ("Tarea")
        verbose_name_plural = ("Tareas")

    def __str__(self):
        return self.nombre


