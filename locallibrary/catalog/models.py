from django.db import models


#importa el modulo models
#que continee la clase models.Model que serviria d base para nuestros modelos
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

#import uuid
# Create your models here.
class provedor(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    direccion = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
       

class pedido(models.Model):
        
    
    nombre = models.CharField(max_length=50)
    id_cliente = models.ForeignKey('Cliente', on_delete=models.SET_NULL, null=True)
    fecha = models.DateField(null=True, blank=True)

    cantidad = models.IntegerField()
    valortotal = models.FloatField()
    id_provedor = models.ForeignKey('provedor', on_delete=models.SET_NULL, null=True)
    valor_ival = models.FloatField()
    valor_neto = models.FloatField()
    
    LOAN_STATUS = (
        ('m', 'proceso'),
        ('o', 'no entregado'),
        ('a', 'entregado'),
        ('r', 'Reserved'),
    )
    estado = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Disponibilidad del libro')
    
    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un autor.
        """
        return reverse('pedido-detalle', args=[str(self.id)])
    

    def __str__(self):
        """
        String que representa al objeto Book
        """
        return self.nombre

   
    
class producto(models.Model):
     nombre = models.CharField(max_length=50)
     pedido = models.ManyToManyField(pedido, help_text="Seleccione un pedido")
     precio = models.FloatField()
     descripcion = models.TextField(max_length=100, help_text="Ingrese una breve descripción del producto")
     
 
     
    
    
class cliente(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono_cliente = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=80)
    email = models.CharField(max_length=80)