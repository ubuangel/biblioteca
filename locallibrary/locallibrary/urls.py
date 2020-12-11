"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    
    #catalog ver rama 
    ramatets creada
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from django.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),#que redirige las peticiones con el patrón catalog/ al módulocatalog.urls (el fichero con el URL relativo /catalog/urls.py).
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),#Ahora redirijamos la URL raíz de nuestro sitio (ej. 127.0.0.1:8000) al URL 127.0.0.1:8000/catalog/
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#eciste un error 4040 
# porque no tenemos ninguna página/url definidas en el módulo catalogs.urls (que es al que nos redirigimos cuando obtenemos la URL a la raíz del sitio). 