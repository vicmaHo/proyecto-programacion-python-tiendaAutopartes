# Autor: Victor Manuel Hernandez
# Fecha: 3 Jul 2022


# Cada funcion cuenta con documentacion la cual indica como funciona y que hace

## FUNCIONES DE COMPROBACION DE DATOS
def comprobacionNumeros(mensaje):
    """Funcion para comprobar si se añadio un numero
    entero."""
    while True:
        try:
            var = int(input(mensaje))
            break
        except:
            print("Ingrese un numero!!\n")
    return var

def comprobacionNumerosFloat(mensaje):
    """Funcion para comprobar si se añadio un numero, flotante 
    o entero"""
    while True:
        try:
            var = float(input(mensaje))
            break
        except:
            print("Ingrese un numero!!\n")
    return var

def comprobacionCaracteres(mensaje):
    """Funcion para comprobar si se añadio un caracter"""
    while True:
        try:
            var = input(mensaje)
            break
        except:
            print("Ingrese una opcion correcta!!\n")
    return var


# FUNCIONES

# Funcion para agregar una espera
def continuarFun():
    """Esta funcion genera en pantalla una espera hasta que el usuario presione enter"""
    input("Presione ENTER para continuar...")

# Funcion del menu de opciones
def menuOpciones():
    """Esta funcion se encarga de desplegar el menu de opciones
    a su vez tambien tiene una entrada con el numero de opcion que
    se desea, y tambien comprueba que esta entrada este en el rango correcto"""
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

# Funcion del menu "Producto o servicio"
def menuProductoSer():
    """Esta funcion despliega un menu el cual sirve para saber 
    si el usuario desea adicionar productos o servicios, tiene un 
    ingreso de datos y comprueba que este ingreso se encuentre en el
    rango correcto"""
    print(" ")
    print("-- Adicionar productos o servicios --")
    print("1. Adicionar PRODUCTO.")
    print("2. Adicionar SERVICIO.")
    print("0. Salir")
    valor = None
    while valor == None:
        valor = comprobacionNumeros("Ingrese la opcion deseada: ")
        if valor not in range(3):
            print("Opcion invalida. Intente nuevamente.")
    return valor

# funcion para agregar un producto
def  adicionarProducto():
    """Esta funcion sirve para adicionar un producto a la matriz 'productos'
    pide 3 ingresos: codigo, descripcion, valor, realiza las comprobaciones correspondientes
    (haciendo uso de las funciones de comprobacion) y añade con un .append un arreglo
    que hace referencia a una nueva fila de la matriz con los datos anteriormente mencionados"""
    while True:
        print(" ")
        print("-- Adicionar producto --")
        codigo = comprobacionNumeros("Ingrese el codigo del producto: ")
        descripcion = input("Ingrese la descripcion del producto: ")
        valor = comprobacionNumerosFloat("Ingrese el valor del producto: ")
        productos.append([codigo,descripcion,valor])
        continuar = input("Desea ingresar otro producto? digite 'n' si no desea agregar otro producto, si desea agregar otro producto digite cualquier letra: ")
        if continuar == "n":
            break

# Funcion para agregar un servicio
def adicionarServicio():
    """Esta funcion sirve para adicionar un servicio a la matriz 'servicios'
    pide 3 ingresos: codigo, descripcion, valor, realiza las comprobaciones correspondientes
    (haciendo uso de las funciones de comprobacion) y añade con un .append un arreglo
    que hace referencia a una nueva fila de la matriz con los datos anteriormente mencionados"""
    while True:
        print(" ")
        print("-- Adicionar servicio --")
        codigo = comprobacionNumeros("Ingrese el codigo del servicio: ")
        descripcion = input("Ingrese la descripcion del servicio: ")
        valor = comprobacionNumerosFloat("Ingrese el valor del servicio: ")
        servicios.append([codigo, descripcion, valor])
        continuar = input("Desea ingresar otro servicio? digite 'n' si no desea agregar otro servicio, si desea agregar otro servicio digite cualquier letra: ")
        if continuar == "n":
            break


# Funcion para asignar encabezados a las matrices de cada orden de trabajo
def asignacionDetitulos(numeroOrden):
    """Con esta funcion se añaden los encabezados 'codigo, tipo, cantidad, valor' a 
    una matriz correspondiente a una orden de trabajo"""
    ordenTrabajo[numeroOrden].append(["Codigo", "Tipo", "Cantidad", "Valor"])

# Funcion para crear una orden de trabajo y añadir productos o servicios a una orden de trabajo
def adicionarOrdenTrabajo():
    """Esta funcion sirve para crear una orden de trabajo y añadirla al diccionario, a su vez haciendo uso de
    la funcion asigancion de titulos, genera la matriz como valor correspondiente a la orden de trabajo, posteriormente
    a esta matriz se le podran agregar productos o servicios que ya han sido ingresados y guardados"""
    while True:
        # Menu de opciones
        print(" ")
        print("-- Adicionar Orden de trabajo --")
        print("1. Agregar orden de trabajo/agregar elementos a una orden de trabajo existente")
        print("0. Salir")
        opcion = comprobacionNumeros("Ingrese una opcion: ")
        # En esta parte se comprueba que existan ordenes de trabajo, si no existen se le pide al usuario crear una nueva,
        # si existen se le mostrara al usuario cuales son, en caso de que desee agregarle productos o servicios
        if opcion == 1:
            if len(ordenTrabajo.keys()) == 0:
                print("\nNo existe ninguna orden de trabajo\n")
            else: 
                print("\n-- Actualmente existen las siguientes ordenes de trabajo --")
                for key in ordenTrabajo.keys():
                    print("Orden Numero:", key)
                print(" ")
            print("Ingrese un numero de orden de trabajo existente para añadir elementos\no ingrese un numero que no existe para crear una nueva orden de trabajo con ese numero.")
            numOrden = comprobacionNumeros("\nIngrese un numero de orden para crearla o añadir elementos: ")
            if numOrden in ordenTrabajo.keys(): # aca comprobamos si el numero ingresado corresponde a una orden de trabajo existente
                print("La orden de trabajo ya existe")
            else:  
                ordenTrabajo[numOrden] = [] # si la orden de trabajo no existe, se crea un arreglo
                asignacionDetitulos(numOrden) # a este arreglo creado se le añade otro arreglo que contiene los encabezados
                print(f"La orden de trabajo {numOrden} ha sido creada\n")
                
            # ahora se le pregunta al usuario si desea agregar elementos a la orden de trabajo anteriormente ingresada
            respuesta = input("Desea agregarle elementos? s/n: ")
            if respuesta == "s":
                while True:
                    print(" ")
                    print("Desea agregar productos o servicios?\n1. Productos\n2. Servicios\n0. Salir") # preguntamos si desea añdir productos o servicios
                    productoOservicio = comprobacionNumeros("Ingrese la opcion: ")
                    if productoOservicio == 1:
                         # si quiere añadir productos(lo mencionado tambien sera lo mismo para servicios)
                         # primero se comprobara que el codigo exista
                        codigo = comprobacionNumeros("Ingrese el codigo del producto: ")
                        codigoNoExiste = True # Se genera esta variable que funcionara para imprimir un mensaje posterirmente en caso de que no exista el codigo
                        for f in range(1, len(productos)): # se realiza un recorrido por las filas, saltandonos la fila 0 ya que esta contiene los encabezados
                            if codigo == productos[f][0]: # recorremos n filas desde la cero, y comprobalos la columna 0, la cual contiene los codigos
                                codigoNoExiste = False  # en caso de que el codigo ingresado coincida con un codigo que ya existe se procedera a pedir los siguientes datos
                                # asigar codigo, tipo, cantidad, valor
                                cantidad = comprobacionNumeros("Ingrese la cantidad del producto: ")
                                tipo = "Producto"
                                valor = cantidad * productos[f][2] # para poder calcular el valor, multiplicamos la cantidad por el dato que corresponde a 
                                                                    # la fila donde se encuentra el codigo y la columna 2, que es el precio del producto o servicio
                                ordenTrabajo[numOrden].append([codigo, tipo, cantidad, valor]) # agregamos al numero de orden, un arreglo que corresponde a una nueva fila
                                                                                                # la cual cual contiene los datos necesarios de una orden de trabajo
                                print("Producto agregado.")
                        if  codigoNoExiste == True:
                            print("El codigo es inexistente. Ingrese nuevamente") # ahora si no se encontro en ningun momento  
                                                                                # un codigo que coincida con el ingresado, quiere decir que no existe
                        
                    # lo explicado anteriormente funciona tambien para la adicion de servicios a la orden de trabajo, solo cambia el 'tipo'
                    elif productoOservicio == 2:
                        codigo = comprobacionNumeros("Ingrese el codigo del servicio: ")
                        codigoNoExiste = True
                        for f in range(1, len(servicios)):
                            if codigo == servicios[f][0]:
                                codigoNoExiste = False
                                cantidad = comprobacionNumeros("Ingrese la cantidad del servicio: ")
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
            elif respuesta == "n":
                break
        else:
            break
    

# funcion que calcula el valor de cierta orden de trabajo
def calcularValorOrdenTrabajo():
    """Esta funcion se encarga de imprimir las ordenes de trabajo existentes, en caso de que hay una
    si no existe se le informa al usuario de que no hay ordenes de trabajo. Se le da a el usuario a elegir 
    la orden de trabajo de la cual quiere calcular su precio, se imprime esta orden de trabajo y se muestra 
    su valor total"""
    print(" ")
    print("-- Calcular el valor de una orden de trabajo --")
    print("Ordenes de trabajo disponibles:")
    if len(ordenTrabajo.keys()) == 0:
        print("No existe ninguna orden de trabajo")
        continuarFun()
    else: 
        for key in ordenTrabajo.keys():
            print("Orden Numero:", key)
        numOrden = comprobacionNumeros("Ingrese el numero de orden para calcular su valor: ")
        print(" ")
        print(f"-- Orden de trabajo numero {numOrden} --")
        mensaje = "" # creamos un mensaje vacio que alamacenara todos los datos de la matriz y los formateara para que parezca una tabla
        # con el siguiente for se recorren todos los datos de la matriz y se almacenan en 'mensaje'
        for f in range(len(ordenTrabajo[numOrden])):
            for c in range(len(ordenTrabajo[numOrden][0])):
                mensaje += str(ordenTrabajo[numOrden][f][c]) + "\t\t\t" # cada dato es transformado a cadena, se le concatenan
                                                                        # tres tabulaciones
            mensaje += "\n" # cuando se acaba una fila, se le concatena un salto de linea para dar orden
        print(mensaje)
        valor = 0
        # el siguiente for recorre las filas de la matriz correspondiente al numero de orden, dejando
        # de lado la fila 0 ya que esta contiene los encabezados, y a la variable
        # acumuladora 'valor' le suma el valor que contiene la fila que se esta iterando y la columna 3, la cual
        # corresponde a el valor de cada producto o servicio dentro de la orden de trabajo
        for f in range(1, len(ordenTrabajo[numOrden])):
                valor += ordenTrabajo[numOrden][f][3]
        print(f"-- Valor de orden de trabajo {numOrden} --")
        print(f"El valor de la orden de trabajo {numOrden} es de: {valor}\n")
        continuarFun()

# funcion para mostrar los productos que se han añadido en forma de tabla
def mostrarProductos():
    """Esta funcion imprime en pantalla una tabla organizada de toda la matriz 'prodcutos'"""
    print(" ")
    print("-- Productos actualmente ingresados -- ")
    mensaje = "" # se genera una variable que contiene una cadena vacia
    # se recorre toda la matriz productos
    for f in range(len(productos)):
        for c in range(len(productos[0])):
            mensaje += str(productos[f][c]) + "\t\t\t" # se convierte a string el dato correspondiente a la fila y 
                                                        # columna iterada se añade a 'mensaje' y se le concatenan 3 tabulaciones
        mensaje += "\n" # cuando acaba de recorrer toda la fila, se le concatena un salto de linea 
    print(mensaje)
    continuarFun()

# funcion para mostrar los servicios que se han añadido en forma de tabla 
# (sigue la misma logica explicada en la funcion mostrarProductos)
def mostrarServicios():
    """Esta funcion imprime en pantalla una tabla organizada de toda la matriz 'servicios'"""
    print(" ")
    print("-- Servicios actualmente ingresados --")
    mensaje = ""
    for f in range(len(servicios)):
        for c in range(len(servicios[0])):
            mensaje += str(servicios[f][c]) + "\t\t\t"
        mensaje += "\n"
    print(mensaje)
    continuarFun()   

# funcion para mostrar las ordenes de trabajo y los elementos que contiene cierta orden previamente seleccionada en forma de tabla
def mostrarOrdenesTrabajo():
    """Esta funcion, nos permite seleccionar una orden de trabajo existente y mostrarnos de forma organizada
    todos los datos de la matriz correspondiente a la orden de trabajo que le indiquemos"""
    print(" ")
    print("-- Mostrar Ordenes de trabajo --")
    print("Ordenes de trabajo actualmente disponilbles:")
    # verifica si existen ordenes de trabajo, en caso de que existan nos muetra una lista con los numeros de estas ordenes
    if len(ordenTrabajo.keys()) == 0:
        print("No existe ninguna orden de trabajo")
    else: 
        for key in ordenTrabajo.keys():
            print("Orden Numero:", key)
        numOrden = comprobacionNumeros("Ingrese el numero de la orden que desea ver: ")
        if numOrden in ordenTrabajo.keys():
            print(" ")
            print(f"-- Orden de trabajo numero {numOrden} --")
            # en esta parte se genera un mensaje vacio, esto sigue la misma logica anteriormente mencionada en la funcion
            # mostrarProductos
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
# matrices que alamacenaran productos y servicios
productos = [["Codigo", "Descripcion", "Valor"]]
servicios = [["Codigo", "Descripcion", "Valor"]]

# en este caso la orden de trabajo sera un diccionario que alamcenara como llave el numero
# de orden y como valor una matriz correspodiente al numero de orden.
ordenTrabajo = {}

# Iniciamos el ciclo principal, el cual se encarga de llamar al menu de opciones
# que retornara un numero que hace referencia a una opcion selecionada
# entonces dependiendo de la opcion seleccionada se ejecutarn las distintas funciones 
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