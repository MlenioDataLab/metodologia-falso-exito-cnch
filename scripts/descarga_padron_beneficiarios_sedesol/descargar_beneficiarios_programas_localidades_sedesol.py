import os
import urllib
import csv


def descargar_localidades(fichero, subdirectorio):
    numero_localidades = 0
    with open(fichero, 'rt') as nombre_fichero:
        numero_localidades = sum(1 for line in nombre_fichero) - 1

    with open(fichero, 'rt') as nombre_fichero:
        fichero_csv = csv.reader(nombre_fichero, delimiter=',', quotechar='"')
        next(fichero_csv)  # ignoramos la primera linea que contiene la cabecera

        for linea in fichero_csv:
            id_localidad = linea[0]
            url = "http://200.77.229.154:8080/ip_cnch/descarga_csv.jsp?cve_loc=" + id_localidad + "&seccion_cnch=PAE3"
            directorio_salida = subdirectorio + "/" + id_localidad[:2]
            fichero_salida = id_localidad + ".csv"

            numero_localidades -= 1

            if numero_localidades % 1000 == 0:
                # Imprimimos cuantas localidades quedan por procesar para ver el progreso, cada 1000 localidades
                print("{} : {}".format(numero_localidades, directorio_salida + "/" + fichero_salida))

            if not os.path.exists(directorio_salida):
                os.makedirs(directorio_salida)

            if not os.path.isfile(directorio_salida + "/" + fichero_salida):
                print(fichero_salida)
                urllib.urlretrieve(url, directorio_salida + "/" + fichero_salida)
            else:
                print("Ya existe " + directorio_salida + "/" + fichero_salida)


descargar_localidades("ids_localidades.csv", "localidades")
