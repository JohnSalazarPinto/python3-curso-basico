"""Variables booleanas"""
var_falso = False
var_verdadero = True
print(var_falso)
print(var_verdadero)
valor_flotante = 3.4
es_entero = valor_flotante.is_integer()
print("El valor es entero?:", es_entero)
"""Variables tuplas"""
mi_tupla_1 = ("Valor1", 10, "valor3")
print(mi_tupla_1)
print(mi_tupla_1[1])
print(mi_tupla_1[0])
"""Objetos"""
auto = {"marca": "Audi", "modelo": "2020"}
print(auto.get("marca"))
print(auto.get("modelo"))

"""IF ELIF ELSE (SI) (O SI) (O)"""
print("### Ejemplo 1 if ###")
var_1 = False

if var_1 == False:
    print(var_1, "ES falso")
elif var_1 == True:
    print(var_1, "ES Verdadero")
else:
    print("No es verdadero ni falso")
print("### Ejemplo 2 if ###")
var_2 = 30

if var_2 > 10:
    print("El valor", var_2, "es mayor a 10")
    print("El valor", var_2, "es mayor a 10")
    print("El valor", var_2, "es mayor a 10")
    if var_2 > 20:
        print("El valor", var_2, "es mayor a 20")
elif var_2 < 10:
    print("El valor", var_2, "es menor a 10")
else:
    print("No es ninguna de las anteriores")

"""Ciclo For"""
print("""Ejemplo For basico""")

lista_2 = [[0, 1, 3, 2],[5, 4, 4, 4]]


print(lista_2[1])

print("""Ejemplo For 1""")

for letra in lista_2:
    print(letra)

print("""Ejemplo For 2""")

for numero in lista_2:
    print(numero)
    for dato in numero:
        print(dato)

print("""Ejemplo For 3""")
print(lista_2[0])
print(lista_2[1])
print("La lista fila 1 y posicion 4: ", lista_2[1][3])

for n in range(len(lista_2)):
    print(n)
    for i in range(len(lista_2[0])):
        lista_2[n][i] = 10

print(lista_2)

