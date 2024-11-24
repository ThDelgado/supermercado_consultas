CUE: CONSULTAS 
DRILLING: PROFUNDIZANDO EN EL MODELO ADMINISTRADOR 



evaluacion 
m7_s7

Para clonar:


Thelma Delgado








		
pasos para instalar DEPENDENCIAS
------------------------------------------

    1-instalar entorno virtual:
        py.exe -m venv venv
    2- activar entorno virtual
        .\venv\scripts\activate
    3- restaurar DEPENDENCIAS
        pip install -r .\requirements.txt



superuser

nombre: admin
email: admin@admin.com
clave: 123456



pruebas elaboraras den vista: listado_productos_view

1 -Obtenga todos los registros de fábricas y productos. 
 System check identified no issues (0 silenced).
November 24, 2024 - 14:57:44
Django version 4.2.16, using settings 'config.settings'       
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

Nombre Champú, Precio: 2500 fabrica: Sin fabrica
Nombre Jabon en polvo, Precio: 3500 fabrica: Sin fabrica      
Nombre Ariel suavizante, Precio: 1800 fabrica: P&G
Nombre Crest Premiun, Precio: 2500 fabrica: P&G
Nombre Crema colgate, Precio: 1500 fabrica: Colgate
Nombre Colgate, Precio: 1450 fabrica: P&G
Nombre Downy Aroma Floral, Precio: 3500 fabrica: P&G
Nombre Protex Aloe, Precio: 1250 fabrica: Colgate
Nombre Speed Stick 24/7, Precio: 4500 fabrica: Colgate        
Nombre Colgate 360, Precio: 1850 fabrica: Colgate
[24/Nov/2024 14:57:50] "GET /inventario/productos HTTP/1.1" 200 6646




2. Obtenga los campos de nombre, precio, y fecha de vencimiento de los productos. Demuestre 
también cuál es la consulta SQL que se genera del ORM. 


C:\workspace_m7\app_supermercado\inventario\views.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 24, 2024 - 15:16:54
Django version 4.2.16, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

C:\workspace_m7\app_supermercado\inventario\views.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...




System check identified no issues (0 silenced).
November 24, 2024 - 15:17:00
Django version 4.2.16, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

Nombre Champú, Precio: 2500 fabrica: Sin fabrica
Nombre Jabon en polvo, Precio: 3500 fabrica: Sin fabrica
Nombre Ariel suavizante, Precio: 1800 fabrica: P&G
Nombre Crest Premiun, Precio: 2500 fabrica: P&G
Nombre Crema colgate, Precio: 1500 fabrica: Colgate
Nombre Colgate, Precio: 1450 fabrica: P&G
Nombre Downy Aroma Floral, Precio: 3500 fabrica: P&G
Nombre Protex Aloe, Precio: 1250 fabrica: Colgate
Nombre Speed Stick 24/7, Precio: 4500 fabrica: Colgate
Nombre Colgate 360, Precio: 1850 fabrica: Colgate
SELECT "productos"."id", "productos"."nombre", "productos"."descripcion", "productos"."precio", "productos"."fabrica_id" FROM "productos"
[24/Nov/2024 15:17:07] "GET /inventario/productos HTTP/1.1" 200 6646




3. Obtenga los productos donde el precio sea menor o igual a 2500, mostrando solo los campos 
de nombre y precio, respectivamente. Demuestra también cuál es la consulta SQL que se 
genera del ORM. 

November 24, 2024 - 15:49:21
Django version 4.2.16, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

<QuerySet [{'nombre': 'Champú', 'precio': 2500}, {'nombre': 'Jabon en polvo', 'precio': 3500}, {'nombre': 'Crest Premiun', 'precio': 2500}, {'nombre': 'Downy Aroma Floral', 'precio': 3500}, {'nombre': 'Speed Stick 24/7', 'precio': 4500}]>
SELECT "productos"."nombre", "productos"."precio" FROM "productos" WHERE "productos"."precio" >= 2500
[24/Nov/2024 15:49:24] "GET /inventario/productos HTTP/1.1" 200 6646




4. Consulte los productos que se vencen antes del año 2024, e imprima el nombre, precio, 
f_vencimiento, y fabricante. Demuestre también cuál es la consulta SQL que se genera del 
ORM. 

November 24, 2024 - 16:12:30
Django version 4.2.16, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

<QuerySet [{'nombre': 'Champú', 'precio': 2500, 'f_vencimiento': datetime.date(2024, 12, 31)}, {'nombre': 'Colgate 360', 'precio': 1850, 'f_vencimiento': datetime.date(2024, 12, 27)}]>
SELECT "productos"."nombre", "productos"."precio", "productos"."f_vencimiento" FROM "productos" WHERE "productos"."f_vencimiento" <= 2024-12-31
[24/Nov/2024 16:12:34] "GET /inventario/productos HTTP/1.1" 200 7138