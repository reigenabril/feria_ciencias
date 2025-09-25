
# src/informar.py

def mostrar_tabla(acumulados, titulo=None):
    """
    Imprime una tabla ordenada por 'puntos' descendente.
    Si viene un 'titulo', lo muestra arriba.
    """
    if titulo:
        print(titulo)
        print("-" * len(titulo))

    encabezado = "Equipo | Innovación | Presentación | Errores | Mejores | Puntos"
    print(encabezado)
    print("-" * len(encabezado))

    filas = sorted(
        acumulados.items(),
        key=lambda item: item[1]["puntos"],
        reverse=True
    )

    for equipo, d in filas:
        print(f"{equipo:7} | {d['innovacion']:10} | {d['presentacion']:12} | "
              f"{d['errores']:7} | {d['mejores']:7} | {d['puntos']:6}")


def mostrar_ganador_de_ronda(nro_ronda, ganador, puntaje):
    """
    Muestra una línea con el mejor equipo de la ronda dada.
    """
    print(f"Ronda {nro_ronda}: el mejor equipo es {ganador} con {puntaje} puntos")


def guardar_csv(acumulados, ruta_csv="ranking.csv"):
    """
    (Opcional) Guarda el ranking en formato CSV.
    """
    import csv
    campos = ["equipo", "innovacion", "presentacion", "errores", "mejores", "puntos"]

    filas = sorted(
        acumulados.items(),
        key=lambda item: item[1]["puntos"],
        reverse=True
    )

    with open(ruta_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(campos)
        for equipo, d in filas:
            writer.writerow([
                equipo, d["innovacion"], d["presentacion"],
                d["errores"], d["mejores"], d["puntos"]
            ])

def mostrar_resultados_finales(acumulados):
    """
    Imprime:
    - Título 'Resultados Finales'
    - 'Equipos Ganadores: ... (N puntos)' (maneja empates)
    - 'Tabla Final de Resultados' con columnas pedidas
    """
    # ordenar por puntos desc
    filas = sorted(
        acumulados.items(),
        key=lambda item: item[1]["puntos"],
        reverse=True
    )

    # ganadores (todos los que empatan en el puntaje máximo)
    max_puntos = filas[0][1]["puntos"] if filas else 0
    ganadores = [eq for eq, d in filas if d["puntos"] == max_puntos]

    # Encabezados
    print("Resultados Finales")
    print(f"Equipos Ganadores: {', '.join(ganadores)} ({max_puntos} puntos)")
    print("Tabla Final de Resultados")

    # Armamos la tabla (alineada)
    encabezado = (
        "Equipo  | Innovación | Presentación | Errores | Mejores | Puntos Total"
    )
    print(encabezado)
    print("-" * len(encabezado))

    for equipo, d in filas:
        print(f"{equipo:7} | {d['innovacion']:10} | {d['presentacion']:12} | "
              f"{d['errores']:7} | {d['mejores']:7} | {d['puntos']:12}")
