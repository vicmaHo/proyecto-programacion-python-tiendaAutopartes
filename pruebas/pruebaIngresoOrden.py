# prueba de la orden de trabajo haciendo uso de diccionarios y
# matrices

# asiganar encabezados a la orden
def asignacionDetitulos(numeroOrden):
    ordenDeTrabajo[numeroOrden].append(["Codigo", "Tipo", "Cantidad", "Valor"])
    

# creo un diccionario vacio
ordenDeTrabajo = {}

# a un numero de orden x, le asigno como valor una lista
ordenDeTrabajo[1] = []

# con la funciona asigacion de tituos creo los titulos
asignacionDetitulos(1)

print(ordenDeTrabajo[1])



print("usted cuenta con estas ordenes de trabajo: ")
print("Numero de orden")
for key in ordenDeTrabajo.keys():
    print(key)
    
    
ordenNum = int(input("Elija el numero de orden de la cual quiere mostrar los elementos: "))

print(f"La orden elejida es la numero {ordenNum}")
print(f"Elementos de la orden de trabajo numero {ordenNum}")
print(ordenDeTrabajo[ordenNum])


# #############ingreso de orde dde trabajo
numAasignar = int(input("Asignele un numero a la orden de trabajo: "))

ordenDeTrabajo[numAasignar] = []
asignacionDetitulos(numAasignar)

print("usted cuenta con estas ordenes de trabajo: ")
print("Numero de orden")
for key in ordenDeTrabajo.keys():
    print(key)
    
ordenNum = int(input("Elija el numero de orden de la cual quiere mostrar los elementos: "))
print(f"La orden elejida es la numero {ordenNum}")
print(f"Elementos de la orden de trabajo numero {ordenNum}")
print(ordenDeTrabajo[ordenNum])


### Ingreso de datos a la orden de trabajo numero...

productos = [
    ["Codigo", "Descripcion", "Valor"],
    [2245, "Llanta", 80000],
    [1009, "Bujia", 30000],
    [2130, "Melasa", 30000]
    ]



# numAasignar = int(input("Asignele un numero a la orden de trabajo: "))

# ordenDeTrabajo[numAasignar] = []
# asignacionDetitulos(numAasignar)

# while True:
#     print(" ")
#     print(f"Es hora de asiganar elementos a la orden de trabajo {numAasignar}")
    
#     productoOservicio= int(input("desea agregar productos o servicios?1. productos - 2. servicios - 0.salir"))
#     if productoOservicio == 1:
#         codigo = int(input("Ingrese el codigo del producto: "))
#         for f in range(1, len(productos)):
#             codigoNoExiste = 0
#             if codigo == productos[f][0]:
#                 codigoNoExiste = 1
#                 # asigar codigo, tipo, cantidad, valor
#                 cantidad = int(input("Ingrese la cantidad del producto: "))
#                 tipo = "Producto"
#                 valor = cantidad * productos[f][2]
#                 ordenDeTrabajo[numAasignar].append([codigo, tipo, cantidad, valor])
#         if  codigoNoExiste == 0:
#             print("El codigo es inexistente. Ingrese nuevamente")
        
#     elif productoOservicio == 2:
#         print("ahora hago esta parte")
#     break


# ordenNum = int(input("Elija el numero de orden de la cual quiere mostrar los elementos: "))
# print(f"La orden elejida es la numero {ordenNum}")
# print(f"Elementos de la orden de trabajo numero {ordenNum}")
# print(ordenDeTrabajo[ordenNum])



while True:
    
    print(" ")
    print("-- Adicionar Orden de trabajo --")
    print("1. Agregar orden de trabajo/agregar elementos")
    print("0. Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        numOrden = int(input("Ingrese un numero para la orden de trabajo: "))
        if numOrden in ordenDeTrabajo.keys():
            print("La orden de trabajo ya existe")
        else:  
            ordenDeTrabajo[numOrden] = []
            asignacionDetitulos(numOrden)
            print(f"La orden de trabajo {numOrden} ha sido creada")
        respuesta = input("Desea agregarle elementos? s/n: ")
        if respuesta == "s":
            while True:
                print(" ")
                print("Desea agregar productos o servicios?\n1. Productos\n2. Servicios\n0. Salir")
                productoOservicio= int(input("Ingrese la opcion: "))
                if productoOservicio == 1:
                    codigo = int(input("Ingrese el codigo del producto: "))
                    codigoNoExiste = 0
                    for f in range(1, len(productos)):
                        if codigo == productos[f][0]:
                            codigoNoExiste = 1
                            # asigar codigo, tipo, cantidad, valor
                            cantidad = int(input("Ingrese la cantidad del producto: "))
                            tipo = "Producto"
                            valor = cantidad * productos[f][2]
                            ordenDeTrabajo[numOrden].append([codigo, tipo, cantidad, valor])
                            print("Producto agregado.")
                    if  codigoNoExiste == 0:
                        print("El codigo es inexistente. Ingrese nuevamente")
                    
                elif productoOservicio == 2:
                    codigo = int(input("Ingrese el codigo del servicio: "))
                    codigoNoExiste = 0
                    for f in range(1, len(productos)):
                        if codigo == productos[f][0]:
                            codigoNoExiste = 1
                            # asigar codigo, tipo, cantidad, valor
                            cantidad = int(input("Ingrese la cantidad del producto: "))
                            tipo = "Producto"
                            valor = cantidad * productos[f][2]
                            ordenDeTrabajo[numOrden].append([codigo, tipo, cantidad, valor])
                            print("Producto agregado.")
                    if  codigoNoExiste == 0:
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
ordenNum = int(input("Elija el numero de orden de la cual quiere mostrar los elementos: "))
print(f"La orden elejida es la numero {ordenNum}")
print(f"Elementos de la orden de trabajo numero {ordenNum}")
print(ordenDeTrabajo[ordenNum])