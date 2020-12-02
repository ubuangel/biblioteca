from django.conf.urls import url

from . import views


urlpatterns = [
 url(r'^$', views.index, name='index'),# view.index una funcion llamada index() en views.py#funcion vista que sera llamda si el patron es detectado
]