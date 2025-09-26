from src.puntuaciones import puntos_totales_acumulados
"""
todas las funciones imprimen resultados parciales y finales o muestran encabezados.
"""

def mostrar_encabezado():
    print("Resultados de la Feria de Ciencias\n")

def mostrar_ronda(indice, mejor_equipo, puntaje):
    print("-" * 80)
    print(f">>> RONDA {indice}")
    print(f"Mejor Equipo de la Ronda:{mejor_equipo} ({puntaje} puntos)")
    print("Ranking Actualizado")

def rondas_restantes(indice):
    restantes = 5 - indice
    if restantes > 0:
        print(f"Rondas restantes: {restantes}")
    else:
        print("No quedan rondas restantes.")


def mostrar_tabla(acumulados):
    encabezado = f"{'Equipo':10} | {'Innovación':10} | {'Presentación':12} | {'Errores':7} | {'Mejores':14} | {'Puntos Total':12}"
    print(encabezado)
    print("-" * len(encabezado))

    equipos_ordenados = sorted(
        acumulados.items(),
        key=lambda par: puntos_totales_acumulados(par[1]),
        reverse=True
    )

    for equipo, datos in equipos_ordenados:
        puntos = puntos_totales_acumulados(datos)
        print(f"{equipo:10} | "
              f"{datos['innovacion']:10} | "
              f"{datos['presentacion']:12} | "
              f"{datos['errores']:7} | "
              f"{datos['mejores']:14} | "
              f"{puntos:12}")
    print()
