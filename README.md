# Metodología

## El (falso) éxito de la Cruzada Nacional contra el Hambre

La Cruzada Nacional Contra el Hambre tiene fallas desde su inicio. Debido a la falta de una metodología para identificar a las personas en pobreza extrema con carencia alimentaria a la cual tiene por mandato beneficiar, en los estados que la concentran se cubre a menos del 40 por ciento, mientras que entidades con pocos pobres alimentarios llegan a tener una cobertura superior al 250 por ciento.

La siguiente metodología explica como se hizo la investigación publicada en:

* [Milenio DataLab](http://www.milenio.com/datalab/falso-exito-Cruzada-Nacional-Hambre_0_696530646.html)
* [Connectas](http://connectas.org/el-falso-exito-de-la-cruzada-contra-el-hambre-en-mexico/)


## Obtención del padrón de beneficiarios

La principal base de datos que utilizamos fue el padrón de beneficiarios de la Cruzada Nacional contra el Hambre, el cual está actualizado al segundo trimestre del 2015.

El padrón es público a a través de sitio de la Cruzada pero se encuentra separado en 304,702 archivos. El usuario únicamente puede consultar un archivo a la vez mediante la selección de entidad, municipio y localidad, lo cual dificulta cualquier tipo de análisis. 

Afortunadamente las ligas de descarga en el servidor de SEDESOL están ordenadas mediante un identificador único que utiliza INEGI para cada localidad del país, lo cual permitió construir un programa que descarga los archivos y los unifica. La base de datos final arroja 4.5 millones de registros.

Es importante destacar que en el proceso de descarga hubo algunas localidades que no pudimos unificar. Cada cierto periodo de tiempo INEGI modifica el catálogo de localidades para reflejar los cambios demográficos en México. En algunas ocasiones se crean identificadores cuando hay nuevos asentamientos y en otras se eliminan identificadores cuando localidades se quedan sin residentes. Esas localidades que no pudimos unificar corresponden a aproximadamente el 0.1% del total del padrón.

El proceso detallado de como descargar el padrón y los scripts necesarios para ello se pueden consultar [aquí](https://github.com/MlenioDataLab/metodologia-falso-exito-cnch/tree/master/scripts/descarga_padron_beneficiarios_sedesol).

## Comparativo entre el padrón de beneficiarios y estimaciones de CONEVAL

En el reportaje se encontró que hay estados donde se beneficia a más personas de la que se debería, mientras que en los más pobres la cobertura es menor al 40%. Para llegar a ese resultado se comparó los datos que utiliza CONEVAL, el organismo encargado de medir la pobreza en México, con los datos del padrón de beneficiarios de la Cruzada.

En las reglas de operación de la Cruzada, publicadas en el Diario Oficial de la Federación, se menciona que la población objetivo la identificaría CONEVAL. Dicha atribución está fundamentada en el artículo 36 Ley General de Desarrollo Social la cual indica que el organismo encargado de definir, medir e identificar la pobreza en México es CONEVAL y son de aplicación obligatoria para todas las entidades federales y dependencias públicas que participen en la ejecución de programas de desarrollo social.

La metodología que utiliza CONEVAL para definir a la población en pobreza extrema con carencia de alimentación es pública y se pueden consultar tanto las bases de datos como los documentos metodológicos en su sitio web.

CONEVAL define la pobreza extrema como aquellas personas cuyo ingreso es tan bajo que no es suficiente para cubrir la canasta básica definida por el gobierno de México, así como presentar tres o más de seis carencias básicas entre las que se incluye salud, educación, vivienda, alimentación, seguridad social y servicios básicos.

Para que una persona sea considerada en pobreza extrema con carencia de alimentación, una de las carencias que sufre debe ser la alimentaria.

En su sitio, CONEVAL tiene registro de las bases de datos que ha utilizado para estimar a dicha población desde el 2010 hasta el 2014. Para nuestro análisis se utilizó la base del 2014, donde se obtuvo el número de personas en pobreza extrema con carencia de alimentación a nivel nacional y por estados, según lo calculó CONEVAL.  Dichos datos son los que está obligado por ley la Cruzada Nacional contra el Hambre a utilizar pues son los que utiliza CONEVAL para su definición y medición.

Para replicar nuestro proceso, basta con agregar los datos del padrón de beneficiarios a nivel estatal o nacional y comparar con los datos del Módulo de Condiciones Socioeconómicas de la Encuesta Nacional de Ingreso y Gasto en los Hogares (ENIGH) que se pueden obtener ya sea en el sitio de INEGI o en el sitio de CONEVAL donde se presenta una versión más limpia de la base.

Las variables de pobreza extrema y de carencias son dicotómicas, por lo cual para calcular la pobreza extrema con carencia de alimentación es necesario contabilizar el número de personas en pobreza extrema a nivel estatal o nacional, condicionado a que una de sus carencias sea la alimentaria.

## Comparativo entre el padrón de beneficiarios y datos a nivel municipal

Los datos de CONEVAL de la Encuesta Nacional de Ingreso y Gasto en los Hogares (ENIGH) sólo puede utilizarse para interpretarse a nivel estatal y nacional, según lo explica CONEVAL en su sitio. A nivel municipal utiliza otra base de datos que proviene del Censo Nacional de Población y Vivienda 2010 y está ajustado por la ENIGH de ese mismo año. La Cruzada está obligada a utilizar esa información con base en la Ley General de Desarrollo Social pues son los últimos estimados que CONEVAL generó para definir pobreza extrema con carencia alimentaria a nivel municipal.

Para realizar el comparativo de cobertura entre los 150 municipios que concentran la mayor proporción de pobreza extrema con carencia de alimentación con aquellos 150 municipios que concentran la menor proporción de pobreza extrema con carencia de alimentación, se necesitó hacer una serie de procesos.

Lo primero que se realizó fue agregar el padrón de beneficiarios a nivel municipal. Dicha variable se dividió por el número de personas en pobreza extrema con carencia de alimentación estimado por CONEVAL para calcular el porcentaje de cobertura.

Lo segundo que se realizó fue seleccionar los 150 municipios que concentran la mayor proporción de pobreza extrema con carencia de alimentación y los 150 municipios que concentran la menor proporción.

El tercer proceso simplemente fue calcular el promedio de cobertura para cada uno de los grupos de 150 municipios, cuyos resultados se presentaron en el artículo.

Es importante destacar que el comparativo que se realizó fue entre una base actualizada a 2010 con una base del 2015 lo cual puede presentar un sesgo de sub o sobre estimación. Sin embargo, al estar obligada la Cruzada por la Ley General de Desarrollo Social a utilizar dichos datos y no exsistir información más actualizada publicada por CONEVAL, nuestro análisis se realizó sujeto al mismo estándar al que debe utilizar SEDESOL para la coordinación de la Cruzada. Existen mecanismos de ajuste que se puden implementar pero dichos mecanismos también presentan sesgos y SEDESOL no está facultada para modificar la estimación provista por CONEVAL.   

## Análisis de cobertura de programas que combaten al hambre

Uno de los principales problemas de la Cruzada Nacional contra el Hambre es que no todos sus beneficiarios reciben programas focalizados al combate de la pobreza y el hambre.

Para analizar dicha información se utilizó el padrón de beneficiarios y el listado de programas. Para cada persona se separó los programas que recibe en columnas independientes de manera que se pueda realizar análisis de cobertura de programas específicos.

Al analizar el listado de programas determinamos que 4 de ellos eran particularmente importantes: Prospera, el principal programa de combate a la pobreza en México; Programa de Apoyo Alimentario, un programa de alimentación para comunidades donde no puede operar Prospera; Comedores Comunitarios, por su amplia expansión y efectividad en proveer de alimentos subsidiados; y Pensiones de Adultos Mayores, las cuales son transferencias económicas a personas mayores de 65 que se pueden utilizar para compra de alimentos.

En el artículo se identificó que 877 mil personas, aproximadamente el 22% del padrón, actualmente no reciben apoyos que directamente combaten la pobreza o el hambre. Para llegar a ese número basta contabilizar todas las personas que no reciben por lo menos uno de los cuatro programas mencionados anteriormente.

## Presupuesto de Prospera y cobertura de personas en pobreza extrema con carencia de alimentación

A través del portal de datos.gob.mx se obtuvo el padrón de beneficiarios de Prospera y PAL donde se indica el nombre del jefe del hogar, lugar de residencia y monto que recibe una familia. Los datos son consistentes con los reportados en el sitio de Prospera donde se indica beneficiar a 6.25 millones de familias.

Puesto que el padrón de beneficiarios de la Cruzada está construido con datos a nivel de persona y no familias, para comparar con el padrón de Prospera fue necesario estimar el número de personas que beneficia Prospera actualmente. Se utilizó la última estimación del Consejo Nacional de Población (CONAPO) el cual indica que una familia promedio en México consiste de 3.7 miembros. Es decir, puesto que actualmente Prospera cubre a 6.25 millones de familias, un estimado conservador indicaría que beneficia a 23.12 millones de personas.

Para estimar que menos del 50% de la población en pobreza extrema con carencia de alimentación actualmente recibe Prospera o PAL, se tiene que calcular la razón entre 3.5 millones de beneficiarios de una población objetivo de 7.1 millones de personas.

## Diferencias entre el padrón de beneficiarios y los datos reportados en el sitio oficial de la Cruzada

Al momento de analizar los datos a nivel de programa del padrón de beneficiarios, nuestro equipo notó que había fuertes discrepancias con los datos que la Cruzada reportaba en su sitio oficial y sus comunicados.

La metodología para contrastar fue sencilla. Simplemente se contrastaron el número de beneficiarios a nivel de programa que se obtuvo del padrón con los datos que se encontraron en el sitio de la Cruzada en la sección de “Mapa”.



