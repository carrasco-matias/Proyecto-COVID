import matplotlib.pyplot as plt
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
# Crear el grafico
def CrearGrafico(ejex, ejey, etiqueta_x, etiqueta_y, titulo, subtitulo):
    plt.plot(ejex,ejey)
    plt.rcParams.update({'figure.autolayout': True})
    plt.xlabel(etiqueta_x)
    plt.ylabel(etiqueta_y)
    plt.title(titulo)
    plt.suptitle(subtitulo)
    plt.show()

def ComunaExiste(cod_comuna):
    datos_linea = LeerArchivo()
    for dato in datos_linea:
        if(dato[3] == cod_comuna):
            return True
    return False

def RegionExiste(cod_region):
    datos_linea = LeerArchivo()
    for dato in datos_linea:
        if(dato[1] == cod_region):
            return True    
    return False

def ContagiadosAcumuladosRegion(cod_region):
    acumulador = 0
    datos_linea = LeerArchivo()
    for dato in datos_linea:
        if(dato[1] == cod_region):
            if(dato[6].strip() == ''):
                acumulador = acumulador + 0
            else:
                acumulador = acumulador + float(dato[6].strip())
    return acumulador

def NombreComuna(cod_comuna):
    datos_linea = LeerArchivo()
    for dato in datos_linea:
        if(dato[3] == cod_comuna):
            return dato[2]    
    return "Desconocida"

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
    # Creación Menu
    print("-------------------------------------------")
    print("Proyecto COVID-19 - Seguimiento de contagios por comuna\n")
    print("[1] Buscar por comuna")
    print("[2] Buscar por región")
    print("[3] Analisis de datos")
    print("[4] Región con mayor y menor nivel de contagio")
    print("[5] Salir\n")
    opcion = input("Ingrese numero de opcion: ")
    # Validar entrada de opcion
    # Se repite mientras la entrada sea distinta de 1, distinta de 2 y distinta de 3
    while(opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5"):
        opcion = input("Ingrese numero de opcion valido: ")
    print("-------------------------------------------")
    # Opciones
    # 1 - Ingresar comuna
    # a) mostrar grafico contagiados no acumulativos ultimos 7 dias de la comuna
    # b) mostrar grafico contagiados acumulativos ultimos 7 dias de la comuna
    if(opcion == "1"):
        opcion = 0
        comuna = input("Ingrese el codigo de la comuna: ")
        if(ComunaExiste(comuna)):
            datos_linea = LeerArchivo()
            while opcion != "3":
                print("[1] GRAFICO CONTAGIADOS NO ACUMULATIVOS")
                print("[2] GRAFICO CONTAGIADOS ACUMULATIVOS")
                print("[3] Salir\n")
                opcion = input("Ingrese numero de opcion: ")
                # Validar entrada de opcion
                # Se repite mientras la entrada sea distinta de 1, distinta de 2 y distinta de 3
                while(opcion != "1" and opcion != "2" and opcion != "3"):
                    opcion = input("Ingrese numero de opcion valido: ")
                print("-------------------------------------------")
                # Graficos
                if(opcion == "1"):
                    # Variables a utilizar en los graficos
                    fechas = list()
                    contagiados = list()
                    ejex = list()
                    ejey = list()
                    
                    print("GRAFICO CONTAGIADOS NO ACUMULATIVOS:")
                    # Datos no acumulados
                    print('Codigo comuna:', comuna)
                    for dato in datos_linea:
                        if(dato[3] == comuna):
                            # grafico de lineas
                            fechas.append(dato[5])
                            contagiados.append(dato[6].strip())
                            # print("Fecha: ", dato[5])
                            # print("Casos no acum.:", dato[6],'\n')
                    # Quedarse con los ultimos 7 valores
                    for i in range(len(fechas)-7, len(fechas)):
                        ejex.append(fechas[i])
                    for i in range(len(contagiados)-7, len(contagiados)):
                        ejey.append(contagiados[i])
                    CrearGrafico(ejex, ejey, 'Fechas', 'Contagiados', 'Contagiados en los ultimos 7 dias', NombreComuna(comuna))
                    opcion = input("Presiona enter para volver.")
                elif(opcion == "2"):
                    print("GRAFICO CONTAGIADOS ACUMULATIVOS:")
                    # Variables a utilizar
                    datos_linea = list()
                    fechas = list()
                    contagiados = list()
                    ejex = list()
                    ejey = list()
                    acumulador = 0
                    datos_linea = LeerArchivo()
                    # Datos acumulados
                    print('Codigo comuna:',comuna)
                    for dato in datos_linea:
                        if(dato[3] == comuna):
                            contagiado = dato[6].rstrip()
                            contagiado = float(contagiado)
                            acumulador = acumulador + contagiado
                            # print("Fecha: ", dato[5])
                            # print("Casos acum.:",acumulador,"\n")
                            fechas.append(dato[5])
                            contagiados.append(acumulador)
                    # Quedarse con los ultimos 7 valores
                    for i in range(len(fechas)-7, len(fechas)):
                        ejex.append(fechas[i])
                    for i in range(len(contagiados)-7, len(contagiados)):
                        ejey.append(contagiados[i])
                    CrearGrafico(ejex, ejey, 'Fechas', 'Contagiados', 'Contagiados en los ultimos 7 dias', NombreComuna(comuna))
                    opcion = input("Presiona enter para volver.")
        else:
            print('Codigo de comuna no existe.')
    # 2 - Ingresar region
    # a) mostrar grafico contagiados no acumulativos ultimos 7 dias de la region
    # b) mostrar grafico contagiados acumulativos ultimos 7 dias de la region
    elif(opcion == "2"):
        opcion = 0
        region = input("Ingrese el codigo de la region: ")
        if(RegionExiste(region)):
            while opcion != "3":
                print("[1] GRAFICO CONTAGIADOS NO ACUMULATIVOS")
                print("[2] GRAFICO CONTAGIADOS ACUMULATIVOS")
                print("[3] Salir\n")
                opcion = input("Ingrese numero de opcion: ")
                # Validar entrada de opcion
                # Se repite mientras la entrada sea distinta de 1, distinta de 2 y distinta de 3
                while(opcion != "1" and opcion != "2" and opcion != "3"):
                    opcion = input("Ingrese numero de opcion valido: ")
                print("-------------------------------------------")
                if(opcion == "1"):
                    print("GRAFICO CONTAGIADOS NO ACUMULATIVOS:")
                    # Variables a utilizar
                    datos_linea = list()
                    fechas = list()
                    contagiados = list()
                    ejex = list()
                    ejey = list()
                    acumulador = 0
                    fecha_en_revision = 0
                    datos_linea = LeerArchivo()
                    # Datos no acumulados
                    print('Codigo region:', region)
                    for dato in datos_linea:
                        if(dato[1] == region):
                            # Si la fecha que se esta revisando es la misma del dato, se acumulan los contagiados
                            if(fecha_en_revision == dato[5]):
                                if(dato[6].strip() == ''):
                                    acumulador = acumulador + 0
                                else:
                                    acumulador = acumulador + float(dato[6].strip())
                            else:
                                # Si es distinta, se almacena la fecha revisada y 
                                # los contagiados acumulados en sus listas correspondientes
                                fechas.append(fecha_en_revision)
                                contagiados.append(acumulador)
                                fecha_en_revision = dato[5]
                                acumulador = 0
                                # Se acumula para no perder los datos
                                if(dato[6].strip() == ''):
                                    acumulador = acumulador + 0
                                else:
                                    acumulador = acumulador + float(dato[6].strip())

                    # Quedarse con los ultimos 7 valores
                    for i in range(len(fechas)-7, len(fechas)):
                        ejex.append(fechas[i])
                    for i in range(len(contagiados)-7, len(contagiados)):
                        ejey.append(contagiados[i])
                    CrearGrafico(ejex, ejey, 'Fechas', 'Contagiados', 'Contagiados en los ultimos 7 dias', NombreRegion(region))
                    opcion = input("Presiona enter para volver.")
                elif(opcion == "2"):        
                    print("GRAFICO CONTAGIADOS ACUMULATIVOS:")
                    # Variables a utilizar
                    datos_linea = list()
                    fechas = list()
                    contagiados = list()
                    ejex = list()
                    ejey = list()
                    acumulador = 0
                    fecha_en_revision = 0
                    datos_linea = LeerArchivo()
                    # Datos acumulados
                    print('Codigo region:',region)
                    for dato in datos_linea:
                        if(dato[1] == region):
                            # Si la fecha que se esta revisando es la misma del dato, se acumulan los contagiados
                            if(fecha_en_revision == dato[5]):
                                if(dato[6].strip() == ''):
                                    acumulador = acumulador + 0
                                else:
                                    acumulador = acumulador + float(dato[6].strip())
                            else:
                                # Si es distinta, se almacena la fecha revisada y 
                                # los contagiados acumulados en sus listas correspondientes
                                fechas.append(fecha_en_revision)
                                contagiados.append(acumulador)
                                fecha_en_revision = dato[5]
                                # Se acumula para no perder los datos
                                if(dato[6].strip() == ''):
                                    acumulador = acumulador + 0
                                else:
                                    acumulador = acumulador + float(dato[6].strip())
                    # Quedarse con los ultimos 7 valores
                    for i in range(len(fechas)-7, len(fechas)):
                        ejex.append(fechas[i])
                    for i in range(len(contagiados)-7, len(contagiados)):
                        ejey.append(contagiados[i])
                    CrearGrafico(ejex, ejey, 'Fechas', 'Contagiados', 'Contagiados en los ultimos 7 dias', NombreRegion(region))
                    opcion = input("Presiona enter para volver.")
        else:
            print('Codigo de region no existe.')
            # 3 - Analisis estadistico de los datos, por comuna o región.
    elif(opcion == "3"):
        acumulador = 0
        regiones = list()
        datos_linea = LeerArchivo()
        for dato in datos_linea:
            if(dato[1] not in regiones and dato[1].isnumeric()):
                regiones.append(dato[1])
        for cod_region in regiones:
            casos = ContagiadosAcumuladosRegion(cod_region)
            print("Casos: ", casos)
            print("Codigo region: ", cod_region)
            print("Nombre region: ", NombreRegion(cod_region))
            print("---------------")
            acumulador = acumulador + casos
        promedio = acumulador/len(regiones) 
        print("Promedio casos acumulados Chile: ", promedio)
        
    # 4 - Región con mayor y menor nivel de contagio (utilizar alguna metrica para comparar)
    elif(opcion == "4"):
        # Listas con las regiones
        regiones = list()
        datos_linea = LeerArchivo()
        for dato in datos_linea:
            if(dato[1] not in regiones and dato[1].isnumeric()):
                regiones.append(dato[1])
        casos_region_mayor = 0
        casos_region_menor = 9999999999
        cod_region_mayor = 0
        cod_region_menor = 0
        for cod_region in regiones:
            casos = ContagiadosAcumuladosRegion(cod_region)
            if(casos > casos_region_mayor):
                casos_region_mayor = casos
                cod_region_mayor = cod_region
            if(casos < casos_region_menor):
                casos_region_menor = casos
                cod_region_menor = cod_region
        # Acumular casos region.
        # Comparar cual es mayor.
        # Acumular casos tercera region
        # Comparar si es mayor la actualmente mayor o la region en revision
        print("REGION CON MENOR NIVEL DE CONTAGIADOS: "+NombreRegion(cod_region_mayor)+", CONTAGIADOS: "+str(casos_region_mayor))
        print("REGION CON MAYOR NIVEL DE CONTAGIADOS: "+NombreRegion(cod_region_menor)+", CONTAGIADOS: "+str(casos_region_menor))
        opcion = input("Presiona enter para volver.")
    else:
        print("SALIR")
        print("-------------------------------------------")