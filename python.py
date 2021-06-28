import matplotlib.pyplot as plt

# Mostrar regiones y comunas en un listado, filtrando dependiendo de la región ingresada por el usuario
# Para buscar los datos de una region o comuna, usuario ingresa su codigo
opcion = 0
# Programa se ejecutará hasta que opcion escogida sea distinta de 5
# archivo_1 = open("","r")
# archivo_2 = open("","r")
archivo = open("Covid-19_std.csv","r")

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
                print("GRAFICO CONTAGIADOS NO ACUMULATIVOS:")
                # Variables a utilizar
                datos_linea = list()
                fechas = list()
                contagiados = list()
                ejex = list()
                ejey = list()
                acumulador = 0
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
                # Datos no acumulados
                print('Codigo comuna:', comuna)
                for dato in datos_linea:
                    if(dato[3] == comuna):
                        # grafico de lineas
                        fechas.append(dato[5])
                        contagiados.append(dato[6])
                        # print("Fecha: ", dato[5])
                        # print("Casos no acum.:", dato[6],'\n')
                # Quedarse con los ultimos 7 valores
                for i in range(len(fechas)-7, len(fechas)):
                    ejex.append(fechas[i])
                for i in range(len(contagiados)-7, len(contagiados)):
                    ejey.append(contagiados[i])
                plt.plot(ejex, ejey)
                plt.xlabel('Ultimas 7 fechas')
                plt.ylabel('Contagiados no acumulados')
                plt.show()
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
                plt.plot(ejex, ejey)
                plt.xlabel('Ultimas 7 fechas')
                plt.ylabel('Contagiados acumulados')
                plt.show()
                opcion = input("Presiona enter para volver.")
    # 2 - Ingresar region
    # a) mostrar grafico contagiados no acumulativos ultimos 7 dias de la region
    # b) mostrar grafico contagiados acumulativos ultimos 7 dias de la region
    elif(opcion == "2"):
        opcion = 0
        region = input("Ingrese el codigo de la region: ")
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
                print("GRAFICO 1")
                opcion = input("Presiona enter para volver.")
            elif(opcion == "2"):        
                print("GRAFICO 2")
                opcion = input("Presiona enter para volver.")
    # 3 - Analisis estadistico de los datos, por comuna o región.
    elif(opcion == "3"):
        opcion = 0
        while opcion != "3":
            print("[1] ANALIZAR DATOS POR COMUNA")
            print("[2] ANALIZAR DATOS POR REGION")
            print("[3] Salir\n")
            opcion = input("Ingrese numero de opcion: ")
            # Validar entrada de opcion
            # Se repite mientras la entrada sea distinta de 1, distinta de 2 y distinta de 3
            while(opcion != "1" and opcion != "2" and opcion != "3"):
                opcion = input("Ingrese numero de opcion valido: ")
            print("-------------------------------------------")
            if(opcion == "1"):
                comuna = input("Ingrese el codigo de la comuna: ")
                print("DATOS 1")
                opcion = input("Presiona enter para volver.")
            elif(opcion == "2"):        
                region = input("Ingrese el codigo de la region: ")
                print("DATOS 2")
                opcion = input("Presiona enter para volver.")
    # 4 - Región con mayor y menor nivel de contagio (utilizar alguna metrica para comparar)
    elif(opcion == "4"):
        opcion = 0
        print("REGION CON MENOR NIVEL DE CONTAGIADOS: , CONTAGIADOS: ")
        print("REGION CON MAYOR NIVEL DE CONTAGIADOS: , CONTAGIADOS: ")
        opcion = input("Presiona enter para volver.")
    else:
        print("SALIR")
        print("-------------------------------------------")