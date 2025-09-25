def puntos_por_equipo(datos_equipo):
    return datos_equipo["innovacion"] * 3 + datos_equipo["presentacion"] - (1 if datos_equipo["errores"] else 0)

def mejor_equipo_ronda(ronda):
    puntajes = {equipo: puntos_por_equipo(datos_equipo) for equipo, datos_equipo in ronda.items()}
    mejor_equipo = max(puntajes, key=puntajes.get)
    return mejor_equipo, puntajes[mejor_equipo]