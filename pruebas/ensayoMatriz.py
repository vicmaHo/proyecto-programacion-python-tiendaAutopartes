# Productos:
# La matriz tiene 3 columnas que son. codigo. descrpcion. valor
# y filas indefinidas ya que no sabemos cuantos productos se van a ingresar



# productos = [["Codigo", "Descripcion", "Valor"]]

# for i in productos:
#     print(i)

# # adicionar datos a la matriz
# while 1:
#     codigo = int(input("Ingrese el codigo del producto: "))
#     descripcion = input("Ingrese la descripcion del producto: ")
#     valor = float(input("Ingrese el valor del producto: "))
    
#     productos.append([codigo,descripcion,valor])
#     continuar = input("s/n: ")
#     if continuar == "n":
#         break
    
# for i in productos:
#     print(i)
    
    
# def mostrarProductos():
#     mensaje = ""
#     for f in range(len(productos)):
#         for c in range(len(productos[0])):
#             mensaje += str(productos[f][c]) + "\t\t"
#         mensaje += "\n"
#     print(mensaje)
    
# print("Mostrar esa vaina")
# mostrarProductos()


productos = [
    ["Codigo", "Descripcion", "Valor"],
    [2245, "Llanta", 80000],
    [1009, "Bujia", 30000]
    
    ]

### ORDEN DE TRABAJO
# esta debe contar con un numero de orden, y a su vez cada numero de orden debe contener
# codigo de producto, tipo, cantidad y valor



ordenTrabajo = [
    ["Numero de orden", 
        ["Codigo", "Tipo", "Cantidad", "Valor"]
    ],
    [1,[productos[1][0], "Producto", 2, productos[1][2]]]
    
    
    ]

# supongamos que el numero de orde nde trabajo sera un entero asigando autommaticamente

#numero de orden de trabajo, orden de trabajo, elemento 
print(ordenTrabajo[1])
print("aqui:  ",ordenTrabajo[0][1])
print(ordenTrabajo[1][1]1[])

for i in range(1, len(ordenTrabajo)):    
    print("Numero  de orden de trabajo: ",ordenTrabajo[i][0])
    for j in range(1, len(ordenTrabajo[0])):
        print("Elementos de la orde de trabajo: ", ordenTrabajo[0][i])
        for k in range(len(ordenTrabajo[0][1])):
            print(ordenTrabajo[1][1][k])




## CON PARALELISMOS

# numeroOrden = ["Numero", 1, 2]
# ordenTrabajo =  [  
#     [
#     ["Codigo", "Tipo", "Cantidad", "Valor"], 
#     [prod]
#     ]
# ]

# for i in range(len(ordenTrabajo)):
#     print(numeroOrden[i])
#     for j in range(len(ordenTrabajo[0])):
#         print(ordenTrabajo[i][j])
        
# acceder a los elementos de la orde de trabajo numero 1
        

