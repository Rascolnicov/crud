from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # La ruta 'leer' en donde listamos todos los registros o jugos de la Base de Datos
    path('jugos/', JugosListado.as_view(template_name = "jugos/index.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un jugo o registro 
    path('jugos/detalle/<int:pk>', JugoDetalle.as_view(template_name = "jugos/detalles.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo jugo o registro  
    path('jugos/crear', JugoCrear.as_view(template_name = "jugos/crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un jugo o registro de la Base de Datos 
    path('jugos/editar/<int:pk>', JugoActualizar.as_view(template_name = "jugos/actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un jugo o registro de la Base de Datos 
    path('jugos/eliminar/<int:pk>', JugoEliminar.as_view(), name='eliminar'), 
]
