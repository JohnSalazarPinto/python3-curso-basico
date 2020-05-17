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

def calcular_area(altura, base):
    """Este metodo calcula el area

    Arguments:
        altura {int} -- Altura en metros
        base {int} -- Ancho del rio en metros
    Returns:
        int -- area en m2
    """
    area = altura * base
    return area

velocidad = calcular_velocidad(distancia, tiempo)
area = calcular_area(altura, base)


def calcular_caudal(velocidad, area):
    """Este metodo calcula el caudal

    Arguments:
        velocidad {int} -- velocidad en metros sobre segundo
        area {int} -- area en metros cuadrados
    Returns:
        int -- caudal en metros cubicos sobre segundo
    """

    caudal = velocidad * area
    return caudal


print("El caudal es:", calcular_caudal(velocidad, area))


def calculo_estabilidad_modelo(delta_x, delta_t):
    """Este metodo calcula la estabilidad

    Arguments:
        delta_x {int} -- Distancia de nodo a nodo en el dominio x
        delta_t {int} -- Paso de tiempo

    Returns:
        int -- Estabilidad a adoptar
    """
    estabilidad = delta_x / delta_t
    if estabilidad > 1:
        estabilidad = 1
    else:
        pass
    return estabilidad

print(calculo_estabilidad_modelo(40, 20))