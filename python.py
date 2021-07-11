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
    # Contenido Grafico, ajuste automatico de la figura
    plt.plot(ejex,ejey)
    plt.rcParams.update({'figure.autolayout': True})
    # Etiquetas Grafico
    plt.xlabel(etiqueta_x)
    plt.ylabel(etiqueta_y)
    # Titulos del grafico
    plt.title(titulo)
    plt.suptitle(subtitulo)
    # Mostrar grafico
    plt.show()
# Validar si el codigo de una comuna existe en el archivo
def FechaExiste(fecha, datos_linea):
    # Recorre lineas del archivo y si encuentra la fecha devuelve True
    for dato in datos_linea:
        if(dato[5] == fecha):
            return True
    return False
# Validar si el codigo de una comuna existe en el archivo
def ComunaExiste(cod_comuna, datos_linea):
    # Recorre lineas del archivo y si encuentra la comuna devuelve True
    for dato in datos_linea:
        if(dato[3] == cod_comuna):
            return True
    return False
# Validar si el codigo de una region existe en el archivo
def RegionExiste(cod_region, datos_linea):
    # Recorre lineas del archivo y si encuentra la region devuelve True
    for dato in datos_linea:
        if(dato[1] == cod_region):
            return True    
    return False
# Devuelve el nombre de la comuna
def NombreComuna(cod_comuna, datos_linea):
    # Recorre lineas del archivo y si encuentra el codigo de la comuna devuelve su nombre
    for dato in datos_linea:
        if(dato[3] == cod_comuna):
            return dato[2]    
    return "Desconocida"
# Devuelve el nombre de la comuna especifica
def NombreComunaDesconocida(cod_comuna, cod_region, datos_linea):
    # Recorre lineas del archivo y si encuentra el codigo de la comuna y la region en la misma fila devuelve su nombre
    for dato in datos_linea:
        if(dato[3] == cod_comuna and dato[1] == cod_region):
            return dato[2]    
    return "Desconocida"
# Devuelve el nombre de la region
def NombreRegion(cod_region, datos_linea):
    # Recorre lineas del archivo y si encuentra el codigo de la region devuelve su nombre
    for dato in datos_linea:
        if(dato[1] == cod_region):
            return dato[0]    
    return "Desconocida"        
opcion = 0
datos_linea = LeerArchivo()
# Programa se ejecutará hasta que opcion escogida sea distinta de 5
while(opcion != "5"):
    opcion = 0
    # --------------- Menu Principal ---------------- #
    print("-------------------------------------------")
    print("Proyecto COVID-19 - Seguimiento de contagios por comuna\n")
    print("[1] Buscar por comuna")
    print("[2] Buscar por region")
    print("[3] Analisis de datos")
    print("[4] Region con mayor y menor nivel de contagio")
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
        if(ComunaExiste(comuna, datos_linea) and comuna != ''):
            nombre_comuna = NombreComuna(comuna, datos_linea)
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
                    # Variables a utilizar
                    fechas = list()
                    contagiados = list()
                    ejex = list()
                    ejey = list()
                    contagiados_hoy = 0
                    contagiados_dia_anterior = 0

                    # Recorrer filas
                    for dato in datos_linea:
                        # Fila es de la comuna ingresada?
                        if(dato[2] == nombre_comuna):
                            contagiados_hoy = dato[6].strip()
                            # Tiene datos de contagiados?
                            if(contagiados_hoy != ''):
                                contagiados_hoy = float(contagiados_hoy)
                                # Se restan los contagiados de hoy con los del dia anterior porque en el archivo los contagiados vienen acumulados.
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
                    
                    # Crear grafico
                    CrearGrafico(ejex, ejey, 'Fechas', 'Contagiados', 'Contagiados no acumulativos en los ultimos 7 dias', nombre_comuna)
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
                        # Fila es de la comuna ingresada?
                        if(dato[2] == nombre_comuna):
                            contagiados_hoy = dato[6].strip()
                            # Contagiados tiene datos?
                            if(contagiados_hoy != ''):
                                contagiados_hoy = float(contagiados_hoy)
                            else:
                                contagiados_hoy = 0
                            # Guardar fecha y contagiados actuales en sus listas
                            fechas.append(dato[5])
                            contagiados.append(contagiados_hoy)
                    
                    # Datos de las ultimas 7 fechas
                    for i in range(len(fechas)-7, len(fechas)):
                        ejex.append(fechas[i])
                    for i in range(len(contagiados)-7, len(contagiados)):
                        ejey.append(contagiados[i])
                    CrearGrafico(ejex, ejey, 'Fechas', 'Contagiados', 'Contagiados acumulativos en los ultimos 7 dias', nombre_comuna)
        else:
            print('Comuna no encontrada.')
    # 2) Buscar por region
    elif(opcion == "2"):
        opcion = 0
        region = input("Ingrese el codigo de la region: ")
        # Validar que el codigo de la region ingresada exista en el archivo
        if(RegionExiste(region, datos_linea)):
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

                    # Listado de fechas y comunas de la region
                    for dato in datos_linea:
                        # Si la comuna es de esta region y no esta agregada a la lista de comunas se agrega
                        if(dato[1] == region and dato[3] not in comunas):
                            comunas.append(dato[3])
                        # Si la fecha no esta agregada a la lista de fechas se agrega
                        if(dato[5] not in listado_fechas):
                            listado_fechas.append(dato[5])
                        
                    # Recorrer filas por fecha
                    for fecha in listado_fechas:
                        suma_contagiados = 0
                        # Por cada comuna
                        for cod_comuna in comunas:
                            nombre_comuna = NombreComunaDesconocida(cod_comuna, region, datos_linea)
                            # Recorrer filas
                            for dato in datos_linea:
                                # Si fila es de la comuna ingresada y de la fecha en revision
                                if(dato[1] == region and dato[2] == nombre_comuna and dato[5] == fecha):
                                    contagiados_hoy = dato[6].strip()
                                    # Tiene datos de contagiados?
                                    if(contagiados_hoy != ''):
                                        contagiados_hoy = float(dato[6].strip())
                                    else:
                                        contagiados_hoy = 0
                                    # Acumular contagiados de la comuna en la fecha de hoy
                                    suma_contagiados = suma_contagiados + contagiados_hoy 
                        # Al terminar de acumular los contagiados de la region
                        # Se restan los contagiados de hoy con los de ayer porque en el archivo los datos vienen acumulados.
                        suma_contagiados_real = suma_contagiados - suma_contagiados_anterior
                        # Se guardan los datos de los contagiados y la fecha en sus listas correspondientes
                        contagiados.append(suma_contagiados_real)
                        fechas.append(fecha)
                        # Se actualiza la suma de los contagiados del dia anterior
                        suma_contagiados_anterior = suma_contagiados

                    # Quedarse con los ultimos 7 valores
                    for i in range(len(fechas)-7, len(fechas)):
                        ejex.append(fechas[i])
                    for i in range(len(contagiados)-7, len(contagiados)):
                        ejey.append(contagiados[i])
                    # Se crea el grafico
                    CrearGrafico(ejex, ejey, 'Fechas', 'Contagiados', 'Contagiados no acumulativos en los ultimos 7 dias', NombreRegion(region, datos_linea))
                # 2) Grafico de contagiados acumulativos de los ultimos 7 dias
                elif(opcion == "2"):
                    print("GRAFICO CONTAGIADOS ACUMULATIVOS:")
                    
                    # Variables a utilizar
                    comunas = list()
                    listado_fechas = list()
                    fechas = list()
                    contagiados = list()
                    ejex = list()
                    ejey = list()
                    contagiados_fecha = 0
                    contagiados_hoy = 0

                    # Listado de fechas y comunas de la region
                    for dato in datos_linea:
                        # Si la comuna es de esta region y no esta agregada a la lista de comunas se agrega
                        if(dato[1] == region and dato[3] not in comunas):
                            comunas.append(dato[3])
                        # Si la fecha no esta agregada a la lista de fechas se agrega
                        if(dato[5] not in listado_fechas):
                            listado_fechas.append(dato[5])
                        
                    # Recorrer filas por fecha
                    for fecha in listado_fechas:
                        suma_contagiados = 0
                        # Se recorre cada comuna
                        for cod_comuna in comunas:
                            nombre_comuna = NombreComunaDesconocida(cod_comuna, region, datos_linea)
                            # Recorrer filas
                            for dato in datos_linea:
                                # Fila es de la comuna ingresada y la fecha en revision
                                if(dato[1] == region and dato[2] == nombre_comuna and dato[5] == fecha):
                                    contagiados_hoy = dato[6].strip()
                                    # Tiene datos de contagiados?
                                    if(contagiados_hoy != ''):
                                        contagiados_hoy = float(dato[6].strip())
                                    else:
                                        contagiados_hoy = 0
                                    # Se acumula la suma de los contagiados
                                    suma_contagiados = suma_contagiados + contagiados_hoy
                        # Al terminar de revisar las comunas de la region se almacenan los datos de los contagiados y la fecha en su lista correspondiente
                        contagiados.append(suma_contagiados)
                        fechas.append(fecha)

                    # Quedarse con los ultimos 7 valores
                    for i in range(len(fechas)-7, len(fechas)):
                        ejex.append(fechas[i])
                    for i in range(len(contagiados)-7, len(contagiados)):
                        ejey.append(contagiados[i])
                    # Se crea el grafico
                    CrearGrafico(ejex, ejey, 'Fechas', 'Contagiados', 'Contagiados acumulativos en los ultimos 7 dias', NombreRegion(region, datos_linea))
        else:
            print('Region no encontrada.')
    # 3) Analisis estadistico (Porcentaje contagiados por comuna)
    elif(opcion == "3"):
        # Variables a utilizar
        regiones = list()
        porcentaje = 0
        
        # Listas con las regiones
        for dato in datos_linea:
            if(dato[1] not in regiones and dato[1].isnumeric()):
                regiones.append(dato[1])
            # Ultima fecha sera la fecha a revisar
            fecha = dato[5]
    
        # Recorrer regiones
        for region in regiones:
            comunas = list()
            
            # Listas con las comunas de esta region
            for dato in datos_linea:
                if(dato[1] == region and dato[3] not in comunas):
                    comunas.append(dato[3])

            # Por cada comuna
            for cod_comuna in comunas:
                nombre_comuna = NombreComunaDesconocida(cod_comuna, region, datos_linea)
                # Recorrer filas
                for dato in datos_linea:
                    # Fila es de la comuna ingresada y la fecha en revision
                    if(dato[1] == region and dato[2] == nombre_comuna and dato[5] == fecha):
                        contagiados_hoy = dato[6].strip()
                        # Tiene datos de contagiados?
                        if(contagiados_hoy != ''):
                            contagiados_hoy = float(dato[6].strip())
                        else:
                            contagiados_hoy = 0
                        poblacion = dato[4]
                        # Tiene datos de poblacion?
                        if(poblacion != '' and poblacion != "0"):
                            # Calcular porcentaje de contagiados de la poblacion
                            porcentaje = (contagiados_hoy*100)/float(poblacion)
                # Mostrar el porcentaje redondeado
                print('Comuna: '+nombre_comuna+'. Porcentaje de la poblacion contagiada: '+str(round(porcentaje))+'%')
        opcion = input("Presiona enter para volver.")
    # 4) Región con mayor y menor nivel de contagio
    elif(opcion == "4"):
        
        # Variables a utilizar
        regiones = list()
        contagiados_hoy = 0
        casos_region_mayor = 0
        casos_region_menor = 9999999999
        cod_region_mayor = 0
        cod_region_menor = 0
        
        # Listas con las regiones
        for dato in datos_linea:
            if(dato[1] not in regiones and dato[1].isnumeric()):
                regiones.append(dato[1])
            # Ultima fecha sera la fecha a revisar
            fecha = dato[5]

        # Recorrer regiones
        for region in regiones:
            comunas = list()
            # Lista con las comunas de la region
            for dato in datos_linea:
                if(dato[1] == region and dato[3] not in comunas):
                    comunas.append(dato[3])
            suma_contagiados = 0
            # Por cada comuna
            for cod_comuna in comunas:
                nombre_comuna = NombreComunaDesconocida(cod_comuna, region, datos_linea)
                # Recorrer filas
                for dato in datos_linea:
                    # Fila es de la comuna ingresada y la fecha en revision
                    if(dato[1] == region and dato[2] == nombre_comuna and dato[5] == fecha):
                        contagiados_hoy = dato[6].strip()
                        # Tiene datos de contagiados?
                        if(contagiados_hoy != ''):
                            contagiados_hoy = float(dato[6].strip())
                        else:
                            contagiados_hoy = 0
                        # Acumular suma de los contagiados
                        suma_contagiados = suma_contagiados + contagiados_hoy
            # Casos de la region son la suma de sus contagiados
            casos = suma_contagiados

            # Comparar cual es mayor o menor. Los casos sumados recientemente o los anteriores
            if(casos > casos_region_mayor):
                casos_region_mayor = casos
                cod_region_mayor = region
            if(casos < casos_region_menor):
                casos_region_menor = casos
                cod_region_menor = region            
        # Mostrar region con mayor y menor nivel de contagiados
        print("Region con mayor nivel de contagiados: "+NombreRegion(cod_region_mayor, datos_linea)+'. Casos: '+str(casos_region_mayor))
        print("Region con menor nivel de contagiados: "+NombreRegion(cod_region_menor, datos_linea)+'. Casos: '+str(casos_region_menor))
        opcion = input("Presiona enter para volver.")
    # 5) Salir
    else:
        print("SALIR")
        print("-------------------------------------------")