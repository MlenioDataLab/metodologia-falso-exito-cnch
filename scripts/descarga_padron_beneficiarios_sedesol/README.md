# Descarga del padrón de beneficiarios

El padrón de beneficiarios se puede consultar en la siguiente dirección web

[Personas en condiciones de pobreza extrema de alimentación que son atendidas por la CNCH](http://sinhambre.gob.mx/personas_en_condiciones_de_pobreza_extrema_de_alimentacion_que_son_atendidas_por_la_cnch/)

Mediante la selección manual de Entidad, Municipio, Localidad es posible consultar uno a uno los municipios en los que hay beneficiarios de la CNCH. Realizar esta tarea para más de 300 mil localidades es a todas luces intensiva en tiempo y propensa a errores.

Es por eso que se desarrollaron scripts para la descarga automatizada de todo el padrón y su posterior consolidación en una sola base de datos.

## Requerimientos técnicos

Los scripts están desarrollados en lenguaje python, usando la versión 2.7 del mismo, por lo cual es necesario tener instalado el entorno de ejecución para poder usar los scripts.

No es el objetivo de este documento explicar como instalar Python. 

## Descarga

Para descargar el padrón de las localidades solo es necesario ejecutar el siguiente script

```Python
python descargar_beneficiarios_programas_localidades_sedesol.py
```

El fichero ids_localidades.csv contiene las claves de las **304,702** localidades.

Si no hay ningún error el script realizará una a una las peticiones de cada localidad, y las irá guardando en carpetas con la siguiente estructura:

```
localidades\{clave_entidad}\{id_localidad}.csv
```

Debido al número de localidades, y dependiendo de la conexión de red y la capacidad de la computadora que ejecute el script, puede tardar al menos 1 hora en descargar el padrón completo.

## Consolidación

Una vez descargado el padrón, para poder procesarlo de una manera más sencilla es necesario consolidar todos los ficheros en uno solo. Para ello es necesario ejecutar el script:

```
python concatenar_localidades.py
```

Este script lee uno por uno los ficheros de las localidades y genera el fichero final **beneficiarios.csv** con todos los datos.


