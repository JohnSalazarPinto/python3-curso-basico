"""Clase 1
"""

altura = input("Ingrese la altura de la seccion: ")
base = input("Ingrese la base de la seccion: ")
distancia = input("Ingrese la distancia del rio: ")
tiempo = input("Ingrese el timpo del flujo: ")

print(altura)
print(base)
print(distancia)
print(tiempo)

def velocidad(distancia, tiempo):
    """Este metodo calcula la velocidad

    Arguments:
        distancia {int} -- Distancia del rio
        tiempo {int} -- Tiempo que tarda la botella en recorrer
                        la distancia del rio

    Returns:
        int -- Velocidad en m/s
    """
    velocidad = distancia * tiempo
    return velocidad