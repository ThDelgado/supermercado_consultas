from django.urls import path
from . import views   

urlpatterns = [
    path('productos', views.listado_productos_view, name= 'listado_productos'),
    path('productos/add', views.add_producto, name="add_producto"),
]