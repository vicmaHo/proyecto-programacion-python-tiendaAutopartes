# programa sin el uso de arquitectura
# programa sin comprobaciones (ignorar una o dos que añadi antes de)
def comprobacionNumeros(mensaje):
    while True:
        try:
            var = int(input(mensaje))
            break
        except:
            print("Ingrese un numero!!")
    return var
# FUNCIONES
def continuarFun():
    input("Presione ENTER para continuar...")

def menuOpciones():
    print(" ")
    print("------ Centro de Servicio Automotriz -------")
    print("Ingrese el NUMERO de la opcion que desea")
    print("1. Adicionar producto/accesorio o servicio")
    print("2. Adicionar Orden de trabajo")
    print("3. Calcular el valor a pagar por una orden de trabajo")
    print("4. Mostrar Productos")
    print("5. Mostrar Servicios")
    print("6. Mostrar ordenes de trabajo")
    print("0. Salir del programa")
    
    valor = None
    while valor == None:
        try:
            valor = int(input("Ingrese una opcion: "))
            if valor not in range(7):
                print("La opcion ingresada es invalida. Ingrese una opcion correcta.")
                valor = None
        except:
            print("Ups, Ingresaste un dato incorrecto\n")
            
    return valor
    
def menuProductoSer():
    print(" ")
    print("-- Adicionar productos o servicios --")
    print("1. Adicionar PRODUCTO.")
    print("2. Adicionar SERVICIO.")
    print("0. Salir")
    valor = None
    while valor == None:
        valor = int(input("Ingrese la opcion deseada: "))
        if valor not in range(3):
            print("Opcion invalida. Intente nuevamente.")
    return valor

def  adicionarProducto():
    while True:
        print(" ")
        print("-- Adicionar producto --")
        codigo = comprobacionNumeros("Ingrese el codigo del producto: ")
        descripcion = input("Ingrese la descripcion del producto: ")
        valor = float(input("Ingrese el valor del producto: "))
        productos.append([codigo,descripcion,valor])
        continuar = input("Desea ingresar otro producto? s/n: ")
        if continuar == "n":
            break

def adicionarServicio():
    while True:
        print(" ")
        print("-- Adicionar servicio --")
        codigo = int(input("Ingrese el codigo del servicio: "))
        descripcion = input("Ingrese la descripcion del servicio: ")
        valor = float(input("Ingrese el valor del servicio: "))
        servicios.append([codigo, descripcion, valor])
        continuar = input("Desea ingresar otro servicio? s/n: ")
        if continuar == "n":
            break

def asignacionDetitulos(numeroOrden):
    ordenTrabajo[numeroOrden].append(["Codigo", "Tipo", "Cantidad", "Valor"])

def adicionarOrdenTrabajo():
    while True:
        print(" ")
        print("-- Adicionar Orden de trabajo --")
        print("1. Agregar orden de trabajo/agregar elementos")
        print("0. Salir")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            numOrden = int(input("Ingrese un numero para la orden de trabajo: "))
            if numOrden in ordenTrabajo.keys():
                print("La orden de trabajo ya existe")
            else:  
                ordenTrabajo[numOrden] = []
                asignacionDetitulos(numOrden)
                print(f"La orden de trabajo {numOrden} ha sido creada")
            respuesta = input("Desea agregarle elementos? s/n: ")
            if respuesta == "s":
                while True:
                    print(" ")
                    print("Desea agregar productos o servicios?\n1. Productos\n2. Servicios\n0. Salir")
                    productoOservicio = int(input("Ingrese la opcion: "))
                    if productoOservicio == 1:
                        codigo = int(input("Ingrese el codigo del producto: "))
                        codigoNoExiste = True
                        for f in range(1, len(productos)):
                            if codigo == productos[f][0]:
                                codigoNoExiste = False
                                # asigar codigo, tipo, cantidad, valor
                                cantidad = int(input("Ingrese la cantidad del producto: "))
                                tipo = "Producto"
                                valor = cantidad * productos[f][2]
                                ordenTrabajo[numOrden].append([codigo, tipo, cantidad, valor])
                                print("Producto agregado.")
                        if  codigoNoExiste == True:
                            print("El codigo es inexistente. Ingrese nuevamente")
                        
                    elif productoOservicio == 2:
                        codigo = int(input("Ingrese el codigo del servicio: "))
                        codigoNoExiste = True
                        for f in range(1, len(servicios)):
                            if codigo == servicios[f][0]:
                                codigoNoExiste = False
                                cantidad = int(input("Ingrese la cantidad del servicio: "))
                                tipo = "Servicio"
                                valor = cantidad * servicios[f][2]
                                ordenTrabajo[numOrden].append([codigo, tipo, cantidad, valor])
                                print("Servicio agregado.")
                        if codigoNoExiste == True:
                            print("El codigo es inexistente. Ingrese nuevamente")
                    elif productoOservicio == 0:
                        print("Saliendo")
                        break
                    else:
                        print("Opcion incorrecta. Ingrese nuevamente")
            else:
                break
        else:
            break
    
def calcularValorOrdenTrabajo():
    print(" ")
    print("-- Calcular el valor de una orden de trabajo --")
    print("Ordenes de trabajo disponibles:")
    if len(ordenTrabajo.keys()) == 0:
        print("No existe ninguna orden de trabajo")
    else: 
        for key in ordenTrabajo.keys():
            print("Orden Numero:", key)
        numOrden = int(input("Ingrese el numero de orden para calcular su valor: "))
        print(" ")
        print(f"-- Orden de trabajo numero {numOrden} --")
        mensaje = ""
        for f in range(len(ordenTrabajo[numOrden])):
            for c in range(len(ordenTrabajo[numOrden][0])):
                mensaje += str(ordenTrabajo[numOrden][f][c]) + "\t\t\t"
            mensaje += "\n"
        print(mensaje)
        valor = 0
        for f in range(1, len(ordenTrabajo[numOrden])):
                valor += ordenTrabajo[numOrden][f][3]
        print(f"-- Valor de orde de trabajo {numOrden} --")
        print(f"El valor de la orden de trabajo {numOrden} es de: {valor}")
        continuarFun()

def mostrarProductos():
    print(" ")
    print("-- Productos actualmente ingresados -- ")
    mensaje = ""
    for f in range(len(productos)):
        for c in range(len(productos[0])):
            mensaje += str(productos[f][c]) + "\t\t\t"
        mensaje += "\n"
    print(mensaje)
    continuarFun()
    
def mostrarServicios():
    print(" ")
    print("-- Servicios actualmente ingresados --")
    mensaje = ""
    for f in range(len(servicios)):
        for c in range(len(servicios[0])):
            mensaje += str(servicios[f][c]) + "\t\t\t"
        mensaje += "\n"
    print(mensaje)
    continuarFun()   

def mostrarOrdenesTrabajo():
    print(" ")
    print("-- Mostrar Ordenes de trabajo --")
    print("Ordenes de trabajo actualmente disponilbles:")
    if len(ordenTrabajo.keys()) == 0:
        print("No existe ninguna orden de trabajo")
    else: 
        for key in ordenTrabajo.keys():
            print("Orden Numero:", key)
        numOrden = int(input("Ingrese el numero de la orden que desea ver: "))
        if numOrden in ordenTrabajo.keys():
            print(" ")
            print(f"-- Orden de trabajo numero {numOrden} --")
            mensaje = ""
            for f in range(len(ordenTrabajo[numOrden])):
                for c in range(len(ordenTrabajo[numOrden][0])):
                    mensaje += str(ordenTrabajo[numOrden][f][c]) + "\t\t\t"
                mensaje += "\n"
            print(mensaje)
        else: 
            print(f"La orden de trabajo {numOrden} no existe.")
    continuarFun()
    
    
## PROGRAMA PRINCIPAL
productos = [["Codigo", "Descripcion", "Valor"]]
servicios = [["Codigo", "Descripcion", "Valor"]]
ordenTrabajo = {}
opcion = None
while opcion == None:
    opcion = menuOpciones()
    if opcion == 1:
        while True:
            producServ = menuProductoSer()
            if producServ == 1:
                adicionarProducto()
                opcion = None
                break
            elif producServ == 2:
                adicionarServicio()
                opcion = None
                break
            elif producServ == 0:
                print("salir al menu principal.")
                opcion = None
                break
    elif opcion == 2:
        adicionarOrdenTrabajo()
        opcion = None
    elif opcion == 3:
        calcularValorOrdenTrabajo()
        opcion = None
    elif opcion == 4:
        mostrarProductos()
        opcion = None
    elif opcion == 5:
        mostrarServicios() 
        opcion = None
    elif opcion == 6:
        mostrarOrdenesTrabajo()
        opcion = None
    elif opcion == 0:
        print("Ha finalizado la ejecucion del programa.")
        break