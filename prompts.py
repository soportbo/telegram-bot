from datetime import datetime
import difflib

# Simula una base de destinos válidos
DESTINOS_VALIDOS = ["Madrid", "Barcelona", "Montevideo", "Buenos Aires", "Paris", "Roma", "Londres", "Nueva York"]

def verificar_destino(destino):
    if destino in DESTINOS_VALIDOS:
        return destino
    similares = difflib.get_close_matches(destino, DESTINOS_VALIDOS, n=3)
    if similares:
        return similares
    return destino

def validar_fechas(fechas):
    try:
        inicio, fin = fechas.split("a")
        fecha_inicio = datetime.strptime(inicio.strip(), "%Y-%m-%d")
        fecha_fin = datetime.strptime(fin.strip(), "%Y-%m-%d")
        return fecha_inicio < fecha_fin and fecha_inicio > datetime.now()
    except Exception:
        return False
