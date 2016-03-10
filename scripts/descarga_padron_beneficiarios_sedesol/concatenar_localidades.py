import os

if os.path.exists("beneficiarios_pobreza_extrema.csv"):
    os.remove("beneficiarios_pobreza_extrema.csv")

fout = open("localidades.csv", "a")
fout.write('"no", "clave_localidad", "nombre_localidad", "nombre", "primer_apellido", "segundo_apellido", "programas"\n')

numero_beneficiarios = 0


def concatenar_ficheros(directorio):
    contador = 0
    for root, directories, filenames in os.walk(directorio):
        for filename in filenames:
            if filename.endswith(".csv"):
                print(os.path.join(root, filename))
                f = open(os.path.join(root, filename))
                f.readlines()
                for line in f:
                    if line.strip():
                        contador += 1
                        fout.write(line)
                f.close()
    return contador


numero_beneficiarios += concatenar_ficheros("localidades")

print(numero_beneficiarios)

fout.close()
