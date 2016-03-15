library(data.table)

beneficiarios <- fread("data/beneficiarios.csv")
programas_sedesol <- fread("data/listado_programas.csv")

anyadir_columnas_programas <- function(beneficiarios, programas_sedesol) {
  numero_beneficiarios <- nrow(beneficiarios)
  nombres_programa_sedesol <- sort(programas_sedesol$nombre_corto)
  for(i in 1:length(nombres_programa_sedesol)) {
    nombre_corto <- nombres_programa_sedesol[i]
    beneficiarios[[nombre_corto]] <- rep(0, numero_beneficiarios)
  }
  return(beneficiarios)
}

beneficiarios <- anyadir_columnas_programas(beneficiarios, programas_sedesol)
beneficiarios[, procesado := FALSE]

start_time <- Sys.time()
beneficiarios_procesados <- 0
beneficiarios_totales <- nrow(beneficiarios)
for(i in 1:nrow(beneficiarios)) {
  procesado <- beneficiarios[i, procesado]
  if(procesado == FALSE) {
    programas_string <- beneficiarios[i, programas]
    programas_beneficiario <- unlist(strsplit(programas_string, split = ", "))
    for(j in 1:length(programas_beneficiario)) {
      beneficiarios[[programas_beneficiario[j]]][i] <- 1
    }
    beneficiarios[i, procesado := TRUE]
  }
  beneficiarios_procesados <- beneficiarios_procesados + 1
  if(i %% 1000 == 0) {
    print(paste(beneficiarios_procesados, beneficiarios_totales, sep = "/"))  
  }
}
end_time <- Sys.time()
print(end_time - start_time)