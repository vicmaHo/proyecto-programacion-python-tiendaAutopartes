OrdenTrabajo = {
    1: [
        ["Codigo", "Tipo", "Cantidad", "Valor"],
        [2130, "Producto", 2, 80000],
        [3021, "Servicio", 1, 30000]
        ], 
    2: [
        ["Codigo", "Tipo", "Cantidad", "Valor"],
        [9088, "Producto", 3, 14500],
        [3002, "Servicio", 5, 30000]
        ]
    }
# el diccionario tiene como llave el numero de orden y como valor una matriz que almacena
# cada uno de los elementos, sean productos o servicios



# mostrar la orde

# print(" ")
# print("-- Mostra Ordenes de trabajo --")
# print("Ordenes de trabajo actualmente disponilbles:")
# print("Numero:")
# for key in diccionario.keys():
#     print("Orden:", key)

# numOrden = int(input("Ingrese el numero de la orden que desea ver: "))
# print(" ")
# print(f"-- Orden de trabajo numero {numOrden} --")
# mensaje = ""
# for f in range(len(diccionario[numOrden])):
#     for c in range(len(diccionario[numOrden][0])):
#         mensaje += str(diccionario[numOrden][f][c]) + "\t\t\t"
#     mensaje += "\n"
# print(mensaje)

diccionario2 = {} 

print(len(diccionario.keys()))
lista = list(diccionario.keys())
print(lista)


# dado el numero de una orden de trabajo se calcule y se muestre el valor a pagar por dicha orden
# imprimir la orden de trabajo y luego el valor de la orden

print(" ")
print("-- Calcular el valor de una orden de trabajo --")
print("Ordenes de trabajo disponibles:")
if len(diccionario.keys()) == 0:
    print("No existe ninguna orden de trabajo")
else: 
    for key in diccionario.keys():
        print("Orden Numero:", key)
    numOrden = int(input("Ingrese el numero de orden para calcular su valor: "))
    print(" ")
    print(f"-- Orden de trabajo numero {numOrden} --")
    mensaje = ""
    for f in range(len(diccionario[numOrden])):
        for c in range(len(diccionario[numOrden][0])):
            mensaje += str(diccionario[numOrden][f][c]) + "\t\t\t"
        mensaje += "\n"
    print(mensaje)
    valor = 0
    for f in range(1, len(diccionario[numOrden])):
            valor += diccionario[numOrden][f][3]
    print(f"-- Valor de orde de trabajo {numOrden} --")
    print(f"El valor de la orden de trabajo {numOrden} es de: {valor}")