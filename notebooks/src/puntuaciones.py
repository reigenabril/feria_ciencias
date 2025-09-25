def puntos_por_equipo(datos_equipo):
    return datos_equipo["innovacion"] * 3 + datos_equipo["presentacion"] - (1 if datos_equipo["errores"] else 0)

def mejor_equipo_ronda(ronda):
    puntajes = {equipo: puntos_por_equipo(datos_equipo) for equipo, datos_equipo in ronda.items()}
    mejor_equipo = max(puntajes, key=puntajes.get)
    return mejor_equipo, puntajes[mejor_equipo]

def inicializar_acumulados(lista_equipos):
    return {
        equipo: {"innovacion": 0,
                 "presentacion": 0,
                 "errores": 0,
                 "mejores": 0,
                 "puntos": 0}
        for equipo in lista_equipos
    }
