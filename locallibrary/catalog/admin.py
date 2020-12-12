from django.contrib import admin
from .models import provedor,pedido,producto,cliente
#La aplicación de administración de Django puede usar tus modelos para construir automáticamente un área dentro del sitio que 
#puedes usar para crear, consultar, actualizar y borrar registros. 

#toda la cnofiguracion para agregar para incluir la aplciacion addmin en tu sitio web 
#fue echa en el esqueleto del projecto
#Registra los modelos copiando el texto siguiente al final del archivo.
# Register your models here.

#Como resultado, todo lo que  debes 
#hacer para agregar tus modelos a la aplicación admin  es  registrarlos
admin.site.register(provedor)
admin.site.register(pedido)
admin.site.register(producto)
admin.site.register(cliente)

#crear super usuario reinicir servidor