
def mostrar_ronda(indice, ronda, mejor_equipo, puntaje, funcion_puntos):
    print(f"\n--- Ronda {indice} ---")
    for equipo, datos in ronda.items():
        print(f"{equipo:10} → {funcion_puntos(datos)} puntos "
              f"(innovación={datos['innovacion']}, "
              f"presentación={datos['presentacion']}, "
              f"errores={datos['errores']})")

    print(f">>> Ganador: {mejor_equipo} con {puntaje} puntos <<<")


def mostrar_resultados_finales(acumulados):
    print("\n--- RESULTADOS FINALES ---")
    print(f"{'Equipo':10} | {'Innovación':10} | {'Presentación':12} | {'Errores':7} | {'Mejores':8} | {'Puntos':6}")
    print("-" * 70)

    for equipo, datos in acumulados.items():
        print(f"{equipo:10} | "
              f"{datos['innovacion']:10} | "
              f"{datos['presentacion']:12} | "
              f"{datos['errores']:7} | "
              f"{datos['mejores']:8} | "
              f"{datos['puntos']:6}")
