def puntos_por_equipo(datos_equipo):
    """
    Calcula el puntaje base de un equipo.
    """
    return datos_equipo["innovacion"] * 3 + datos_equipo["presentacion"] - (1 if datos_equipo["errores"] else 0)

def mejor_equipo_ronda(ronda):
    """
    determina el mejor equipo usando `max`
    """
    puntajes = {equipo: puntos_por_equipo(datos_equipo) for equipo, datos_equipo in ronda.items()}
    mejor_equipo = max(puntajes, key=puntajes.get)
    return mejor_equipo, puntajes[mejor_equipo]

def inicializar_acumulados(lista_equipos):
    """
    arranca la planilla con todos los contadores en 0.
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
    usa filter para sumar errores y actualiza los acumulados.
    """
    equipos_con_errores = filter(lambda eq: ronda[eq]["errores"], ronda)
    for equipo in equipos_con_errores:
        acumulados[equipo]["errores"] += 1

    for equipo, datos_equipo in ronda.items():
        acumulados[equipo]["innovacion"] += datos_equipo["innovacion"]
        acumulados[equipo]["presentacion"] += datos_equipo["presentacion"]
        acumulados[equipo]["puntos"] += puntos_por_equipo(datos_equipo)
    acumulados[mejor_equipo]["mejores"] += 1