##Importamos las librerias necesarias
from bs4 import BeautifulSoup
import requests
import time 

##Funcion #1
def scraping_enlaces_manual(url):
    
    ##Creamos listas vacias
    nombres_productos = []
    precios_productos = []
    link_productos = []
    plataforma_productos = [] 
    
    ##Iniciamos un bucle 
    while True:
        
       # Creamos una condicion dentro de un bucle para validar que el enlace ingresado sea valido.
       # Esto previene errores al momento de hacer la solicitud, si el enlace está mal escrito, incompleto o pertenece a una plataforma que no funciona en este proceso.
       if (not url.startswith("https://www.masonline.com.ar/") and not url.startswith("https://atomoconviene.com/")
           and not url.startswith("https://articulo.mercadolibre.com.ar/") and not url.startswith("https://www.mercadolibre.com.ar/") 
           and not url.endswith("html ") and not url.endswith("p ")):
           print("Lo ingresado no es valido!")
           url = input("Ingrese el enlace del producto: ").strip().lower()
       else:
           ##Creamos una variable con la identificacion (informacion del navegador) que va solicitar el servidor para identificarnos y hacemos la solicitud
           dispositivo = "Mozilla/5.0 (iPhone; CPU iPhone OS 17_7_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Mobile/15E148 Safari/604.1"
           contenido_pagina_web = requests.get(url, headers={"User-Agent": dispositivo}) 
           
           ##Procesamos los datos extraidos de la pagina 
           procesar_pagina_web = BeautifulSoup(contenido_pagina_web.text, "lxml")
           
           #Dependiendo de la estructura HTML de cada plataforma, la forma en que extraemos los datos cambian
           #Para eso creamos varias condiciones para cada plataforma.
           #Atomo 
           if url.startswith("https://atomoconviene.com/atomo-ecommerce/"):
              ##Extraemos lo datos, en este caso nombre y precio del producto
              nombre = procesar_pagina_web.find_all("h1", class_="h1") 
              precio = procesar_pagina_web.find_all("span", class_="current-price-display price") 
              print("Sitio Atomo")
              #Agregamos a las listas el nombre de la plataforma y el enlace
              plataforma_productos.append("Atomo") 
              link_productos.append(url)
              
           #MasOnline  
           if url.startswith("https://www.masonline.com.ar/"):
               print("Sitio MasOnline")
               plataforma_productos.append("Masonline")
               link_productos.append(url)
               nombre = procesar_pagina_web.find_all("span", class_="vtex-store-components-3-x-productBrand")
               precio = procesar_pagina_web.find_all("span", class_="valtech-gdn-dynamic-product-1-x-currencyContainer")
               
           #MercadoLibre    
           if url.startswith("https://articulo.mercadolibre.com.ar/") or url.startswith("https://www.mercadolibre.com.ar/"):
              print("Sitio Mercadolibre")
              plataforma_productos.append("Mercadolibre")
              link_productos.append(url)
              nombre = procesar_pagina_web.find_all("h1", class_="ui-pdp-title") 
              precio = procesar_pagina_web.find_all("span", class_="andes-money-amount__fraction") 
           
           #Con for leemos y guardamos lo extraidos en sus listas
           for nombre_1 in nombre:
               nombres_productos.append(nombre_1.text)
               print("Se agrego con exito el producto:", nombre_1.text) #Hacemos un sprint de los productos que el usuario va guardando
           for precio_1 in precio:
               precios_productos.append(precio_1.text)
               print("Se agrego con exito el producto:", precio_1.text)
               break ##agregamos el primero valor y cerramos el bucle. Lo hacemos para evitar que agregue mas de un elemento a la lista.
               
           #Consulta al usuario si quiere continuar
           url = input("Ingrese el enlace del producto o salir para terminar: ").strip().lower()
           if url == "salir":
               break #Cerramos el bucle
           else:
               print("Cargando....")
               time.sleep(3) ##Agregamos un tiempo de espera de 3 seg para evitar baneos
               print("Cargando.....")
    return nombres_productos, precios_productos, link_productos, plataforma_productos 

#Funcion #2
#Similar a la funcion #1, pero en este caso, el usuario ingresa un archivo de formato (.txt). 
#Esto lo hace mas automatico, solamente creamos unas variables con fila inicial (0) y fila final (Utilizamos len para leer la cantidad de filas)
#Una vez termine el primer recorrido, se le sumara a la variable  el valor (1) y con la otra variable la utilizaremos como condicion para terminar el bucle.
def scraping_enlaces_txt(lista):
    nombres_productos = []
    precios_productos = []
    link_productos = []
    plataforma_productos = []
    
    #Variables que se utilizaran para el while y el recorrido de cada fila de la lista
    fila_inicial = 0 
    fila_final = len(lista)
    
    #Tambien se agrego una variable que calcula la cantidad de segundo que va tardar en terminar en finalizar todo el proceso
    estimacion_en_segundos = fila_final * 3
    print("Hay una estimacion de", estimacion_en_segundos, "Segundos.")
    
    #Inicio de bucle
    while fila_inicial < fila_final:
        
       url = lista[fila_inicial]
       
       if (not url.startswith("https://www.masonline.com.ar/") and not url.startswith("https://atomoconviene.com/")
           and not url.startswith("https://articulo.mercadolibre.com.ar/") and not url.startswith("https://www.mercadolibre.com.ar/") 
           and not url.endswith("html ") and not url.endswith("p ")):
           print("Error, el enlace numero", fila_inicial, "no es valido!")
           print("Enlace no valido:",url)
           print("Cargando siguiente enlace....")
           
           fila_inicial += 1 
       else:
           dispositivo = "Mozilla/5.0 (iPhone; CPU iPhone OS 17_7_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Mobile/15E148 Safari/604.1"
           contenido_pagina_web = requests.get(url, headers={"User-Agent": dispositivo}) 
           procesar_pagina_web = BeautifulSoup(contenido_pagina_web.text, "lxml")
           
           if url.startswith("https://atomoconviene.com/atomo-ecommerce/"):
              nombre = procesar_pagina_web.find_all("h1", class_="h1") 
              precio = procesar_pagina_web.find_all("span", class_="current-price-display price") 
              print("Sitio Atomo")
              plataforma_productos.append("Atomo")
              link_productos.append(url)
              
           if url.startswith("https://www.masonline.com.ar/"):
               print("Sitio MasOnline")
               plataforma_productos.append("Masonline")
               link_productos.append(url)
               nombre = procesar_pagina_web.find_all("span", class_="vtex-store-components-3-x-productBrand")
               precio = procesar_pagina_web.find_all("span", class_="valtech-gdn-dynamic-product-1-x-currencyContainer")
           
           if url.startswith("https://articulo.mercadolibre.com.ar/") or url.startswith("https://www.mercadolibre.com.ar/"):
              print("Sitio Mercadolibre")
              plataforma_productos.append("Mercadolibre")
              link_productos.append(url)
              nombre = procesar_pagina_web.find_all("h1", class_="ui-pdp-title") 
              precio = procesar_pagina_web.find_all("span", class_="andes-money-amount__fraction")
              
           for nombre_1 in nombre:
               nombres_productos.append(nombre_1.text)
               print("Se agrego con exito el producto:", nombre_1.text)
           for precio_1 in precio:
               precios_productos.append(precio_1.text)
               print("Se agrego con exito el producto:", precio_1.text)
               break 
           
           print("Cargando....")
           time.sleep(3) 
           print("Cargando.....")
           
           fila_inicial += 1  #Sumamos el valor (1) para pasar al siguiente enlace de la lista
           
    return nombres_productos, precios_productos, link_productos, plataforma_productos
    
    
    













































