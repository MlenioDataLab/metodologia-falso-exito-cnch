# Separar programas de beneficiarios

La información del padrón contiene una columna en la que de manera agregada indica que programas recibe cada beneficiario, una cadena de texto separada por comas con cada uno de los programas. Este formato es muy dificil de procesar.

Se hace necesario separar los programas, cada uno en una columna, para poder analizar mejor la información.

El script **separar_programas.R** se encarga de leer el fichero **data/beneficiarios.csv** y separar los programas en columnas independientes.

El fichero **beneficiarios.csv** se obtiene después de descargar y consolidar el padrón mediante los [scripts de esta sección](https://github.com/milenio-datalab/metodologia-falso-exito-cnch/tree/master/scripts/descarga_padron_beneficiarios_sedesol).

Para comodidad de quien no quiera realizar la descarga, se incluye el fichero de **beneficiarios.csv** comprimido y separado en varios ficheros 7z.

Ejecutar el script que separa los programas es intensivo en cálculo, ya que el código no está optimizado y el dataset contiene más de 4 millones de registros y puede tardar algunas horas en ejecutarse.

Para comodidad de quien no quiera realizar el procesamiento, incluimos el dataset final de beneficiarios en la carpeta **data/resultado_final/** como un conjunto de ficheros comprimidos 7z. El dataset final descomprimido pesa 1.4 GB.
