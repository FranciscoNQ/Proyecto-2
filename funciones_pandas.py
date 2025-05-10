##Importamos liberias
import pandas as pd
import datetime as dt

##Creamos variables con la ruta de la carpeta para abrir y guardar dataset.
path = "C:/Users/nicol/Desktop/proyecto #2/dataset/" 
path_2 = "C:/Users/nicol/Desktop/proyecto #2/archivo txt/" 

##Funcion #1
def guardar_dataset(nombres_productos, precios_productos, link_productos, plataforma_productos):
    consulta_dataset_nombre = str(input("Ingrese un nombre para el dataset: ")).strip()
    while consulta_dataset_nombre == "":
        consulta_dataset_nombre = str(input("Ingrese un nombre: ")).strip()
    else:
        consulta_dataset_formato = str(input("Seleccione el formato\n1. csv\n2. Excel\n:"))
        while consulta_dataset_formato != "1" and consulta_dataset_formato != "2" and consulta_dataset_formato != "3":
            print("Lo ingresado no es valido, recuerda ingresar solamente el numero!")
            consulta_dataset_formato = str(input("Seleccione el formato\n1. csv\n2. Excel\n:"))
        else:
            ##Creamos un diccionario con las listas
            data = {"Producto" : nombres_productos,  
                    "Precio" : precios_productos,
                    "Link" : link_productos,
                    "Plataforma" : plataforma_productos}  
            df = pd.DataFrame(data) ##Lo convertimos a dataframe
            df["Fecha"] = dt.date.today() ##Agregamos una columna con la fecha actual usando la libreria datetime
            df.drop_duplicates(keep = "first", inplace= True) ##Borramos las filas duplicadas
            ##Ordenamos las columnas
            columns = ["Producto", "Precio", "Fecha","Plataforma", "Link"]  
            df = df[columns]
            ##lo guardamos en el formato que el usuario eligio, borrando el index.
            if  consulta_dataset_formato == "1":
                df.to_csv(path+consulta_dataset_nombre+"_crudo.csv", index = False)
            if  consulta_dataset_formato == "2":
                df.to_excel(path+consulta_dataset_nombre+"_crudo.xlsx", index = False) 

#Funcion #2                
def entrada_dataset_txt(nombre_archivo):
    df_text = pd.read_csv(path_2+nombre_archivo+".txt", header=None) #Lo convertimos a dataframe
    lista = df_text.iloc[:, 0].tolist() #Creamos una lista y guardamos todas las filas
    return lista 
     
     
