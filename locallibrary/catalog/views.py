from django.shortcuts import render

# Create your views here.
from .models import  provedor, producto, pedido,cliente

def index(request):
    """
    Función vista para la página inicio del sitio.
    
    """
    
    provedor=provedor.objects.all().count()
    producto=producto.objects.count()  # El 'all()' esta implícito por defecto.
    cliente=cliente.objects.all().count()   
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_provedor':num_provedor,'num_pedido':num_pedido,'num_producto':num_producto,'num_cliente':num_cliente},
    )
    
#def book(request):
    