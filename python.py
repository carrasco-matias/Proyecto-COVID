# Mostrar regiones y comunas en un listado, filtrando dependiendo de la región ingresada por el usuario
# Para buscar los datos de una region o comuna, usuario ingresa su codigo
# opcion = 0
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
            if(opcion == "1"):
                print("GRAFICO CONTAGIADOS NO ACUMULATIVOS")
                opcion = input("Presiona enter para volver.")
            elif(opcion == "2"):        
                print("GRAFICO 2")
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