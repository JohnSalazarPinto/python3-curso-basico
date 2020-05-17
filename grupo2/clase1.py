"""Clase 1
"""

altura = int(input("Ingrese la altura de la seccion: "))
base = int(input("Ingrese la base de la seccion: "))
distancia = int(input("Ingrese la distancia del rio: "))
tiempo = int(input("Ingrese el timpo del flujo: "))


def calcular_velocidad(distancia, tiempo):
    """Este metodo calcula la velocidad

    Arguments:
        distancia {int} -- Distancia del rio en metros
        tiempo {int} -- Tiempo en segundos que tarda la botella en recorrer
                        la distancia del rio 

    Returns:
        int -- Velocidad en m/s
    """
    velocidad = distancia / tiempo
    return velocidad


print(calcular_velocidad(distancia, tiempo))
print(calcular_velocidad(50, 20))
print(calcular_velocidad(50, 10))
print(calcular_velocidad(50, 50))