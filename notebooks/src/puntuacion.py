def puntos_por_equipo(datos_equipo):
    """
    Calcula los puntos de un equipo en una ronda.
    datos_equipo es un diccionario con:
      - 'innovacion': puntos de innovación
      - 'presentacion': puntos de presentación
      - 'errores': True si se equivocaron, False si no
    Reglas:
      * cada punto de innovación vale 3
      * cada punto de presentación vale 1
      * si hubo errores, se resta 1
    Devuelve el puntaje total de ese equipo.
    """
    puntos_base = datos_equipo["innovacion"] * 3 + datos_equipo["presentacion"]
    descuento = 1 if datos_equipo["errores"] else 0
    puntaje_final = puntos_base - descuento
    return puntaje_final

def mejor_equipo_ronda(ronda):
    """
    Devuelve el nombre del equipo y su puntaje en una ronda,
    pero solo del que salió primero (el mejor).
    
    Parámetro:
      - ronda: un diccionario con la forma {equipo: datos_equipo}
        donde cada equipo tiene sus puntos de 'innovacion',
        'presentacion' y 'errores'.

    Qué hace:
      * Calcula el puntaje de todos los equipos usando la función puntos_por_equipo.
      * Busca cuál es el puntaje más alto.
      * Devuelve el nombre del mejor equipo y sus puntos.
    
    Ejemplo:
      Si ronda = {"EquipoA": {"innovacion": 2, "presentacion": 3, "errores": True}}
      entonces devuelve ("EquipoA", 8).
    """
    puntajes = {equipo: puntos_por_equipo(datos_equipo) for equipo, datos_equipo in ronda.items()}
    mejor_equipo = max(puntajes, key=puntajes.get)
    return mejor_equipo, puntajes[mejor_equipo]

def inicializar_acumulados(lista_equipos):
    """
    Arma la planilla de acumulados desde cero.

    Recibe:
      - lista_equipos: una lista con los nombres de los equipos.

    Devuelve:
      Un diccionario con cada equipo como clave y otro diccionario
      adentro con sus contadores, todos en 0:
        - 'innovacion'
        - 'presentacion'
        - 'errores'
        - 'mejores'  (cuántas veces fue el mejor de la ronda)
        - 'puntos'   (puntaje total acumulado)
    """
    return {
        equipo: {"innovacion": 0,
                 "presentacion": 0,
                 "errores": 0,
                 "mejores": 0,
                 "puntos": 0}
        for equipo in lista_equipos
    }


def actualizar_acumulados(acumulados, ronda, mejor_equipo):
    """
    Suma los resultados de una ronda dentro de la planilla general.

    Recibe:
      - acumulados: diccionario con los contadores de todos los equipos.
      - ronda: diccionario con los resultados de esa ronda {equipo: datos_equipo}.
      - mejor_equipo: el nombre del equipo que ganó la ronda.

    Qué hace:
      * Va sumando los puntos de 'innovacion', 'presentacion' y 'errores'.
      * Calcula el puntaje de la ronda con la función puntos_por_equipo
        y lo acumula en 'puntos'.
      * Al mejor equipo le suma 1 en 'mejores' (cantidad de veces que fue ganador).
    """
    for equipo, datos_equipo in ronda.items():
        acumulados[equipo]["innovacion"] += datos_equipo["innovacion"]
        acumulados[equipo]["presentacion"] += datos_equipo["presentacion"]
        acumulados[equipo]["errores"] += int(datos_equipo["errores"])
        acumulados[equipo]["puntos"] += puntos_por_equipo(datos_equipo)

    acumulados[mejor_equipo]["mejores"] += 1

