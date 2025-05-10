## Proyecto #2 - Bot de Scraping para Supermercados (MercadoLibre, Atomo, MasOnline)

Bot de scraping desarrollado en Python que permite extraer datos de productos (nombre y precio) desde plataformas de supermercados  como MercadoLibre, Átomo y MasOnline (Por el momento, solo funciona con esos tres), con solo ingresar el enlace del producto.

Al finalizar el proceso, los datos se guardan con pandas en un dataset que incluye: nombre del producto, precio, enlace, plataforma y fecha de extracción, luego se exporta en formato Excel o CSV, según la elección del usuario.

Todo el proceso se realiza a través de un menú interactivo que guía paso a paso al usuario para crear su propio dataset con información de las plataformas disponibles.

## librerías y tecnologías 

- Python: Lenguaje principal del proyecto.
- Pandas: Entrada, transformación y exportacion del dataset.
- Request: Realizar solicitudes y obtener la informacion HTML de cada enlace.
- BeautifulSoup: Procesar el HTML extraído.
- Time: Utilizado para agregar una pausa en cada solicitud.
- Datatime: Registrar fecha actual en el dataset.

## Notas

- Este bot está pensado para uso personal
- Las estructuras HTML pueden cambiar, por lo que podría ser necesario actualizar el código si alguna plataforma modifica su diseño.



