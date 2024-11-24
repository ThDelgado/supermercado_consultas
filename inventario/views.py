from django.shortcuts import render, redirect
from .models import Producto, Fabrica 

from .forms import ProductoFormAdd
from django.contrib import messages
from django.utils import timezone


# Create your views here.
   
           
def listado_productos_view(request):
    contexto = {}
    productos = Producto.objects.all()
    
    contexto["productos"] = productos
     
    #for producto in productos:
    #    print(f"Nombre {producto.nombre}, Precio: {producto.precio} fabrica: {producto.fabrica}")
    #
    #print(str(productos.query))       
    
    #filtro = Producto.objects.filter(precio__gte=2500).values('nombre','precio')
    #print(filtro)
    #print(str(filtro.query))
    
    filtro = Producto.objects.filter(f_vencimiento__lte="2024-12-31").values('nombre','precio','f_vencimiento')
    print(filtro)
    print(str(filtro.query))

    return render(request, "inventario/listado_productos.html", contexto)

    
def add_producto(request):
    contexto = {}
        
    if request.method == 'GET':
        contexto["form"] = ProductoFormAdd()
        return render(request, 'inventario/add_producto.html', contexto)
    
    if request.method == 'POST':   #
        
        form = ProductoFormAdd(request.POST)
        contexto["form"] = form 
        
        print(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, "Producto creado correctamente.")
            return redirect('listado_productos')
            
        else:
            messages.error(request, "Algo ha fallado, revise bien los datos ingresados.")
            return render(request, 'inventario/add_producto.html', contexto)
  