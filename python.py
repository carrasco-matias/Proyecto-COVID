# Importar libreria para graficos
import matplotlib.pyplot as plt
# ------- Funciones --------- #
# Leer archivo
def LeerArchivo():
    datos_linea = list()
    # Abrir el archivo en modo lectura
    archivo = open('Covid-19_std.csv', 'r')
    # Devuelve una lista de las lineas leidas del archivo
    lineas = archivo.readlines()
    # Cerrar archivo.
    archivo.close()
    # Recorrer cada linea en la lista entregada por la lectura del archivo
    for linea in lineas:
        # Transforma cada elemento separado por una coma en una lista y se agrega a datos_linea
        datos_linea.append(linea.split(','))
    return datos_linea
# Crear grafico
def CrearGrafico(ejex, ejey, etiqueta_x, etiqueta_y, titulo, subtitulo):
    plt.plot(ejex,ejey)
    plt.rcParams.update({'figure.autolayout': True})
    plt.xlabel(etiqueta_x)
    plt.ylabel(etiqueta_y)
    plt.title(titulo)
    plt.suptitle(subtitulo)
    plt.show()
# Validar si el codigo de una comuna existe en el archivo
def FechaExiste(fecha):
    datos_linea = LeerArchivo()
    for dato in datos_linea:
        if(dato[5] == fecha):
            return True
    return False
# Validar si el codigo de una comuna existe en el archivo
def ComunaExiste(cod_comuna):
    datos_linea = LeerArchivo()
    for dato in datos_linea:
        if(dato[3] == cod_comuna):
            return True
    return False
# Validar si el codigo de una region existe en el archivo
def RegionExiste(cod_region):
    datos_linea = LeerArchivo()
    for dato in datos_linea:
        if(dato[1] == cod_region):
            return True    
    return False
# Devuelve el nombre de la comuna
def NombreComuna(cod_comuna):
    datos_linea = LeerArchivo()
    for dato in datos_linea:
        if(dato[3] == cod_comuna):
            return dato[2]    
    return "Desconocida"
# Devuelve el nombre de la region
def NombreRegion(cod_region):
    datos_linea = LeerArchivo()
    for dato in datos_linea:
        if(dato[1] == cod_region):
            return dato[0]    
    return "Desconocida"        
opcion = 0
# Programa se ejecutará hasta que opcion escogida sea distinta de 5
while(opcion != "5"):
    opcion = 0
    # --------------- Menu Principal ---------------- #
    print("-------------------------------------------")
    print("Proyecto COVID-19 - Seguimiento de contagios por comuna\n")
    print("[1] Buscar por comuna")
    print("[2] Buscar por region")
    print("[3] Analisis de datos")
    print("[4] Región con mayor y menor nivel de contagio")
    print("[5] Salir\n")
    opcion = input("Ingrese numero de opcion: ")
    # Validar entrada de opcion
    while(opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5"):
        opcion = input("Ingrese numero de opcion valido: ")
    print("-------------------------------------------")
    # --------------- Opciones ---------------- #
    # 1) Buscar por comuna
    if(opcion == "1"):
        opcion = 0
        comuna = input("Ingrese el codigo de la comuna: ")
        # Validar que el codigo de la comuna ingresada exista en el archivo
        if(ComunaExiste(comuna) or comuna == ''):
            datos_linea = LeerArchivo()
            nombre_comuna = NombreComuna(comuna)
            # --------------- Menu Comuna ---------------- #
            while opcion != "3":
                print("[1] GRAFICO CONTAGIADOS NO ACUMULATIVOS")
                print("[2] GRAFICO CONTAGIADOS ACUMULATIVOS")
                print("[3] Salir\n")
                opcion = input("Ingrese numero de opcion: ")
                # Validar entrada de opcion
                while(opcion != "1" and opcion != "2" and opcion != "3"):
                    opcion = input("Ingrese numero de opcion valido: ")
                print("-------------------------------------------")
                # 1) Grafico de contagiados no acumulativos por comuna de los ultimos 7 dias
                if(opcion == "1"):
                    # Variables a utilizar en los graficos
                    fechas = list()
                    contagiados = list()
                    ejex = list()
                    ejey = list()
                    contagiados_hoy = 0
                    contagiados_dia_anterior = 0

                    # Recorrer filas
                    for dato in datos_linea:
                        # Fila es de la comuna ingresada
                        if(dato[2] == nombre_comuna):
                            # tiene datos de contagiados?
                            contagiados_hoy = dato[6].strip()
                            if(contagiados_hoy != ''):
                                contagiados_hoy = float(contagiados_hoy)
                                contagiados_fecha = contagiados_hoy - contagiados_dia_anterior
                                # Guardar fecha y contagiados actuales en sus listas
                                contagiados.append(contagiados_fecha)
                                fechas.append(dato[5])
                                contagiados_dia_anterior = contagiados_hoy
                                
                    # Datos de las ultimas 7 fechas
                    for i in range(len(fechas)-7, len(fechas)):
                        ejex.append(fechas[i])
                    for i in range(len(contagiados)-7, len(contagiados)):
                        ejey.append(contagiados[i])
                    CrearGrafico(ejex, ejey, 'Fechas', 'Contagiados', 'Contagiados no acumulativos en los ultimos 7 dias', NombreComuna(comuna))
                # 2) Grafico de contagiados acumulativos por comuna de los ultimos 7 dias
                elif(opcion == "2"):
                    print("GRAFICO CONTAGIADOS ACUMULATIVOS:")
                    # Variables a utilizar
                    fechas = list()
                    contagiados = list()
                    ejex = list()
                    ejey = list()
                    contagiados_hoy = 0

                    # Recorrer filas
                    for dato in datos_linea:
                        # Fila es de la comuna ingreada
                        if(dato[2] == nombre_comuna):
                            # Guardar fecha y contagiados actuales en sus listas
                            contagiados_hoy = dato[6].strip()
                            if(contagiados_hoy != ''):
                                contagiados_hoy = float(contagiados_hoy)
                            else:
                                contagiados_hoy = 0
                            fechas.append(dato[5])
                            contagiados.append(contagiados_hoy)
                    # Quedarse con los ultimos 7 valores
                    for i in range(len(fechas)-7, len(fechas)):
                        ejex.append(fechas[i])
                    for i in range(len(contagiados)-7, len(contagiados)):
                        ejey.append(contagiados[i])
                    CrearGrafico(ejex, ejey, 'Fechas', 'Contagiados', 'Contagiados acumulativos en los ultimos 7 dias', NombreComuna(comuna))
        else:
            print('Comuna no encontrada.')
    # 2) Buscar por region
    elif(opcion == "2"):
        opcion = 0
        region = input("Ingrese el codigo de la region: ")
        # Validar que el codigo de la region ingresada exista en el archivo
        if(RegionExiste(region)):
            datos_linea = LeerArchivo()
            # --------------- Menu region ---------------- #
            while opcion != "3":
                print("[1] GRAFICO CONTAGIADOS NO ACUMULATIVOS")
                print("[2] GRAFICO CONTAGIADOS ACUMULATIVOS")
                print("[3] Salir\n")
                opcion = input("Ingrese numero de opcion: ")
                # Validar entrada de opcion
                while(opcion != "1" and opcion != "2" and opcion != "3"):
                    opcion = input("Ingrese numero de opcion valido: ")
                print("-------------------------------------------")
                # 1) Grafico de contagiados no acumulativos de los ultimos 7 dias
                if(opcion == "1"):
                    print("GRAFICO CONTAGIADOS NO ACUMULATIVOS:")
                    
                    # Variables a utilizar
                    datos_linea = LeerArchivo()
                    comunas = list()
                    listado_fechas = list()
                    fechas = list()
                    contagiados = list()
                    ejex = list()
                    ejey = list()
                    contagiados_hoy = 0
                    suma_contagiados = 0
                    suma_contagiados_anterior = 0
                    suma_contagiados_real = 0

                    # Listas con las comunas de esta region
                    for dato in datos_linea:
                        if(dato[1] == region and dato[3] not in comunas):
                            comunas.append(dato[3])
                    
                    # Listado de fechas
                    for dato in datos_linea:
                        if(dato[5] not in listado_fechas):
                            listado_fechas.append(dato[5])

                    # Recorrer filas por fecha
                    for fecha in listado_fechas:
                        suma_contagiados = 0
                        # Por cada comuna
                        for cod_comuna in comunas:
                            nombre_comuna = NombreComuna(cod_comuna)
                            # Recorrer filas
                            for dato in datos_linea:
                                # Fila es de la comuna ingresada
                                if(dato[2] == nombre_comuna and dato[5] == fecha):
                                    # Tiene datos de contagiados?
                                    contagiados_hoy = dato[6].strip()
                                    if(contagiados_hoy != ''):
                                        contagiados_hoy = float(dato[6].strip())
                                    else:
                                        contagiados_hoy = 0
                                    suma_contagiados = suma_contagiados + contagiados_hoy 
                        suma_contagiados_real = suma_contagiados - suma_contagiados_anterior
                        contagiados.append(suma_contagiados_real)
                        fechas.append(fecha)
                        suma_contagiados_anterior = suma_contagiados

                    # Quedarse con los ultimos 7 valores
                    for i in range(len(fechas)-7, len(fechas)):
                        ejex.append(fechas[i])
                    for i in range(len(contagiados)-7, len(contagiados)):
                        ejey.append(contagiados[i])
                    CrearGrafico(ejex, ejey, 'Fechas', 'Contagiados', 'Contagiados no acumulativos en los ultimos 7 dias', NombreRegion(region))
                # 2) Grafico de contagiados acumulativos de los ultimos 7 dias
                elif(opcion == "2"):
                    print("GRAFICO CONTAGIADOS ACUMULATIVOS:")
                    
                    # Variables a utilizar
                    datos_linea = LeerArchivo()
                    comunas = list()
                    listado_fechas = list()
                    contagiados_fecha = 0
                    contagiados_hoy = 0
                    fechas = list()
                    contagiados = list()
                    ejex = list()
                    ejey = list()

                    # Listas con las comunas
                    for dato in datos_linea:
                        if(dato[1] == region and dato[3] not in comunas):
                            comunas.append(dato[3])
                    
                    # Listado de fechas
                    for dato in datos_linea:
                        if(dato[5] not in listado_fechas):
                            listado_fechas.append(dato[5])
                    
                    # Recorrer filas por fecha
                    for fecha in listado_fechas:
                        suma_contagiados = 0
                        # Por cada comuna
                        for cod_comuna in comunas:
                            nombre_comuna = NombreComuna(cod_comuna)
                            # Recorrer filas
                            for dato in datos_linea:
                                # Fila es de la comuna ingresada
                                if(dato[2] == nombre_comuna and dato[5] == fecha):
                                    # Tiene datos de contagiados?
                                    contagiados_hoy = dato[6].strip()
                                    if(contagiados_hoy != ''):
                                        contagiados_hoy = float(dato[6].strip())
                                    else:
                                        contagiados_hoy = 0
                                    suma_contagiados = suma_contagiados + contagiados_hoy
                        contagiados.append(suma_contagiados)
                        fechas.append(fecha)

                    # Quedarse con los ultimos 7 valores
                    for i in range(len(fechas)-7, len(fechas)):
                        ejex.append(fechas[i])
                    for i in range(len(contagiados)-7, len(contagiados)):
                        ejey.append(contagiados[i])
                    CrearGrafico(ejex, ejey, 'Fechas', 'Contagiados', 'Contagiados acumulativos en los ultimos 7 dias', NombreRegion(region))
        else:
            print('Region no encontrada.')
    # 3) Analisis estadistico
    elif(opcion == "3"):
        # Porcentaje contagiados por region
        # Listas con las regiones
        datos_linea = LeerArchivo()
        comunas = list()
        porcentaje = 0
        # Listas con las comunas
        for dato in datos_linea:
            if(dato[3] not in comunas and dato[3].isnumeric()):
                comunas.append(dato[3])
        # Acumular casos region.
        for cod_comuna in comunas:
            # Recorrer filas
            for dato in datos_linea:
                if(dato[3] == cod_comuna):
                    poblacion = float(dato[4])
                    if(dato[6].strip() == ''):
                        casos = 0
                    else:
                        casos = float(dato[6].strip())
                    if(poblacion != 0):
                        porcentaje = (casos*100)/poblacion
            print('Comuna: '+NombreComuna(cod_comuna)+'. Porcentaje de la poblacion contagiada: '+str(round(porcentaje))+'%')
        opcion = input("Presiona enter para volver.")
    # 4) Región con mayor y menor nivel de contagio
    elif(opcion == "4"):
        datos_linea = LeerArchivo()
        regiones = list()
        casos_region_mayor = 0
        casos_region_menor = 9999999999
        cod_region_mayor = 0
        cod_region_menor = 0
        casos_hoy = 0
        # Listas con las regiones
        for dato in datos_linea:
            if(dato[1] not in regiones and dato[1].isnumeric()):
                regiones.append(dato[1])
        # Acumular casos region.
        for cod_region in regiones:
            # CASOS ACUMULADOS POR REGION ULTIMO DIA
            # ---------------------------------------
            # Recorrer filas
            for dato in datos_linea:
                # Fila es de la region ingreada?
                if(dato[1] == cod_region):
                    # Fecha 
                    if(dato[6].strip() == ''):
                        casos_hoy = casos_hoy + 0
                    else: 
                        casos_hoy = casos_hoy + float( dato[6].strip() )
            casos = casos_hoy
            # Comparar cual es mayor.
            if(casos > casos_region_mayor):
                casos_region_mayor = casos
                cod_region_mayor = cod_region
            if(casos < casos_region_menor):
                casos_region_menor = casos
                cod_region_menor = cod_region
        
        print("Region con mayor nivel de contagiados: "+NombreRegion(cod_region_mayor))
        print("Region con menor nivel de contagiados: "+NombreRegion(cod_region_menor))
        opcion = input("Presiona enter para volver.")
    # 5) Salir
    else:
        print("SALIR")
        print("-------------------------------------------")