"""Curso de Python"""
print("Hola Mundo!")

numero_entero = 10
numero_flotante = 10.1
print(numero_entero)
print(numero_flotante)

"""El comando type() sirve para 
    ver el tipo de la variable """

numero_entero_tipo = type(numero_entero)
numero_flotante_tipo = type(numero_flotante)

print(numero_entero_tipo)
print(numero_flotante_tipo)

print("##############")

var_1 = 10
var_2 = 50 
resultado = var_1 * var_2
print(resultado)

print("##############")

"""Variable tipo String(Cadena)"""

palabra_1 = "Hola Mundo!"
palabra_2 = 'Hola Mundo2!'
print(palabra_1)
print(palabra_2)
print(type(palabra_1))
print(type(palabra_2))

print("##############")

nombre = "Adhemar"
edad = 20
print("El nombre de", nombre, "es:", edad)

print("##############")

"""Variables tipo listas []"""

lista_1 = [nombre, edad, numero_flotante_tipo]
print(lista_1)
print(lista_1[0])
print(lista_1[1])
print(lista_1[2])

lista_2 = [lista_1, 25, 15.9, "palabra en lista"]
print(lista_2)
print(lista_2[0])
print(lista_2[1])
print(lista_2[2])
print(lista_2[3])
print("De la lista_1 la posicion 0:", lista_2[0][0])



