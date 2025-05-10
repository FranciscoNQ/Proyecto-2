##Importamos los modulos de las funciones
from funcion_scraping import scraping_enlaces_manual, scraping_enlaces_txt
from funciones_pandas import guardar_dataset, entrada_dataset_txt

#lista para utilizar como condicion
numeros_condiciones = ["1", "2", "3"]

#Presentacion
print("Bienvenido!!!\nEsta script solo funciona con los sitios web de Atomo, MasOnline y Mercadolibre!!!")
consulta = str(input("Menu:\n1. Enlaces de las plataformas\n2. Crear dataset\n3. Salir\nIngrese el numero de su eleccion: "))

#Inciamos un bucle con while True para el menu principal
while True:
    
    #Creamos varias condiciones, algunas validan que el usuario seleccione alguna opcion valida, caso contrario, estara en un bucle hasta ingresar una opcion valida
    #Otras son para consultar las plataformas disponible, mostrando el enlace oficial
    #Y las restantes permiten crear el dataset o salir del programa si el usuario no desea continuar.

    if consulta not in numeros_condiciones: 
        print("Lo ingresado no es valido, ingrese el numero de la opcion que seleccione")
        consulta = str(input("Menu:\n1. Enlaces de las plataformas\n2. Crear dataset\n3. Salir\nIngrese el numero de su eleccion: "))
        
    if consulta == "1":    
        print("Sitios:\n1) https://atomoconviene.com/\n2) https://www.masonline.com.ar/\n3) https://articulo.mercadolibre.com.ar/")
        consulta = str(input("Menu:\n1. Enlaces de las plataformas\n2. Crear dataset\n3. Salir\n: "))
        
    if consulta == "2":
        consulta_dataset = str(input("\nOpciones: \n1. Ingresar los enlaces manualmente(uno por uno)\n2. Ingresar un archivo con formato (.txt) con los enlaces\n: "))
        
        while consulta_dataset not in numeros_condiciones:
           print("Lo ingresado no es valido, ingrese el numero de la opcion que seleccione")
           consulta_dataset = str(input("Opciones: \n1. Ingresar los enlaces manualmente(uno por uno)\n2. Ingresar un archivo con formato (.txt) con los enlaces\n: "))
           
        if consulta_dataset == "1":
           url = input("Ingrese el enlace del producto: ").strip().lower()
           
           nombres_productos, precios_productos, link_productos, plataforma_productos = scraping_enlaces_manual(url)
           
           guardar_dataset(nombres_productos, precios_productos, link_productos, plataforma_productos)
           
           print("La dataset fue guardado con exito!!")
           print("Redirigiendo al menu principal....")
           consulta = str(input("Menu:\n1. Enlaces de las plataformas\n2. Crear dataset\n3. Salir\nIngrese el numero de su eleccion: "))
           
        if consulta_dataset == "2":
            print("\nInstrucciones para subir el archivo:\n1. El archivo debe ser un bloc de nota (Formato .txt)")
            print("2. Los enlaces deben estar ordenado, uno debajo del otro")
            nombre_archivo = input("Ingrese el nombre del archivo(debe figura igual, incluyendo mayusculas y espacios): ").strip()
            
            lista = entrada_dataset_txt(nombre_archivo)
            
            nombres_productos, precios_productos, link_productos, plataforma_productos = scraping_enlaces_txt(lista)
            
            guardar_dataset(nombres_productos, precios_productos, link_productos, plataforma_productos)
            
            print("La dataset fue guardado con exito!!")
            print("Redirigiendo al menu principal....")
            consulta = str(input("Menu:\n1. Enlaces de las plataformas\n2. Crear dataset\n3. Salir\nIngrese el numero de su eleccion: "))
            
    if consulta == "3":
        break #Forzamos el cierre del bucle inicial

#Fin 
print("Cerrando....")
print("Cerrado con exito!!")  

