from datetime import datetime

# Lista de temas
temas = [
    {"Tema": "El Temblor", "Fecha Lanzamiento": "2017-03-12", "Vistas": "45.8 millones", "Duracion": "235", "Link": "https://www.youtube.com/watch?v=A1B2C3D4E5"},
    {"Tema": "Mi Libertad", "Fecha Lanzamiento": "2017-07-25", "Vistas": "37.4 millones", "Duracion": "210", "Link": "https://www.youtube.com/watch?v=F6G7H8I9J0"},
    {"Tema": "Tu Mejor Estudiante", "Fecha Lanzamiento": "2018-05-14", "Vistas": "52.6 millones", "Duracion": "248", "Link": "https://www.youtube.com/watch?v=K1L2M3N4O5"},
    {"Tema": "FMK | Estani | Rusherking - Bandido", "Fecha Lanzamiento": "2022-09-10", "Vistas": "64.2 millones", "Duracion": "320", "Link": "https://www.youtube.com/watch?v=P6Q7R8S9T0"},
    {"Tema": "Karina - No Me Digas que No", "Fecha Lanzamiento": "2022-11-21", "Vistas": "58.3 millones", "Duracion": "298", "Link": "https://www.youtube.com/watch?v=U1V2W3X4Y5"},
    {"Tema": "Mario Luis - Whisky", "Fecha Lanzamiento": "2022-08-15", "Vistas": "41.7 millones", "Duracion": "245", "Link": "https://www.youtube.com/watch?v=Z6A7B8C9D0"},
    {"Tema": "FMK - Tu 50", "Fecha Lanzamiento": "2022-06-05", "Vistas": "49.9 millones", "Duracion": "260", "Link": "https://www.youtube.com/watch?v=E1F2G3H4I5"},
    {"Tema": "Tengo en Venta el Corazón", "Fecha Lanzamiento": "2023-02-18", "Vistas": "32.1 millones", "Duracion": "275", "Link": "https://www.youtube.com/watch?v=J6K7L8M9N0"},
    {"Tema": "Esa Morocha", "Fecha Lanzamiento": "2023-04-12", "Vistas": "27.5 millones", "Duracion": "230", "Link": "https://www.youtube.com/watch?v=O1P2Q3R4S5"},
    {"Tema": "Ulises Bueno | Los Palmeras | Migrantes - Atorrante", "Fecha Lanzamiento": "2023-07-19", "Vistas": "78.4 millones", "Duracion": "360", "Link": "https://www.youtube.com/watch?v=T6U7V8W9X0"},
    {"Tema": "La Konga | Antonio Ríos - Adicto", "Fecha Lanzamiento": "2023-09-09", "Vistas": "53.9 millones", "Duracion": "310", "Link": "https://www.youtube.com/watch?v=Y1Z2A3B4C5"},
    {"Tema": "J mena | Karina | Angela Torres - Sinvergüenza", "Fecha Lanzamiento": "2023-11-22", "Vistas": "60.7 millones", "Duracion": "295", "Link": "https://www.youtube.com/watch?v=D6E7F8G9H0"},
    {"Tema": "Angel López | Rusherking - A Puro Dolor", "Fecha Lanzamiento": "2024-01-15", "Vistas": "34.8 millones", "Duracion": "305", "Link": "https://www.youtube.com/watch?v=I1J2K3L4M5"},
    {"Tema": "BM | Mario Luis | Onda Sabanera - Ladrona", "Fecha Lanzamiento": "2024-03-10", "Vistas": "29.6 millones", "Duracion": "280", "Link": "https://www.youtube.com/watch?v=N6O7P8Q9R0"},
    {"Tema": "Chernobyl", "Fecha Lanzamiento": "2019-06-08", "Vistas": "15.2 millones", "Duracion": "215", "Link": "https://www.youtube.com/watch?v=S1T2U3V4W5"},
    {"Tema": "Pastillitas", "Fecha Lanzamiento": "2020-10-30", "Vistas": "18.7 millones", "Duracion": "220", "Link": "https://www.youtube.com/watch?v=X6Y7Z8A9B0"},
    {"Tema": "Como Vos Lo Haces", "Fecha Lanzamiento": "2021-02-13", "Vistas": "21.5 millones", "Duracion": "265", "Link": "https://www.youtube.com/watch?v=C1D2E3F4G5"},
    {"Tema": "Estani - Sola", "Fecha Lanzamiento": "2021-08-29", "Vistas": "25.3 millones", "Duracion": "255", "Link": "https://www.youtube.com/watch?v=H6I7J8K9L0"},
    {"Tema": "Rusherking - Porque Puedo", "Fecha Lanzamiento": "2022-03-07", "Vistas": "36.8 millones", "Duracion": "310", "Link": "https://www.youtube.com/watch?v=M1N2O3P4Q5"},
    {"Tema": "Quien es Quien", "Fecha Lanzamiento": "2022-12-12", "Vistas": "33.9 millones", "Duracion": "245", "Link": "https://www.youtube.com/watch?v=R6S7T8U9V0"},
    {"Tema": "La Konga | Karina - Manicomio", "Fecha Lanzamiento": "2023-05-17", "Vistas": "40.4 millones", "Duracion": "295", "Link": "https://www.youtube.com/watch?v=W1X2Y3Z4A5"},
    {"Tema": "Karina | Angela - WTF", "Fecha Lanzamiento": "2023-10-05", "Vistas": "23.0 millones", "Duracion": "225", "Link": "https://www.youtube.com/watch?v=B6C7D8E9F0"}
]

# Funciones auxiliares
def obtener_colaboradores(titulo: str) -> list:
    if "-" not in titulo:
        return []
    parte_colaboradores = titulo.split("-")[0]
    lista_colaboradores = parte_colaboradores.split("|")
    return [colaborador.strip() for colaborador in lista_colaboradores]

def obtener_nombre_tema(titulo: str) -> str:
    return titulo.split("-")[-1].strip()

def convertir_vistas_numerico(vistas: str) -> int:
    return int(float(vistas.split()[0]) * 1_000_000)

def convertir_duracion_numerico(duracion: str) -> int:
    return int(duracion)

def obtener_codigo(url: str) -> str:
    return url.split("=")[-1]

def formatear_fecha(fecha: str) -> datetime:
    return datetime.strptime(fecha, "%Y-%m-%d")

# Funciones principales
def normalizar_datos(temas: list) -> list:
    temas_normalizados = []
    for tema in temas:
        tema_normalizado = {
            "Tema": obtener_nombre_tema(tema["Tema"]),
            "Colaboradores": obtener_colaboradores(tema["Tema"]),
            "Fecha Lanzamiento": formatear_fecha(tema["Fecha Lanzamiento"]),
            "Vistas": convertir_vistas_numerico(tema["Vistas"]),
            "Duracion": convertir_duracion_numerico(tema["Duracion"]),
            "Link": tema["Link"],
            "Codigo": obtener_codigo(tema["Link"])
        }
        temas_normalizados.append(tema_normalizado)
    return temas_normalizados

def mostrar_temas(temas: list):
    print("\nLista de temas:")
    for tema in temas:
        print(f"- {tema['Tema']} | Fecha: {tema['Fecha Lanzamiento'].strftime('%Y-%m-%d')}")

def ordenar_temas(temas: list) -> list:
    return sorted(temas, key=lambda x: x["Duracion"], reverse=True)

def calcular_promedio_visitas(temas: list) -> float:
    total_vistas = sum(tema["Vistas"] for tema in temas)
    return (total_vistas / len(temas)) / 1_000_000

def calcular_maxima_reproduccion(temas: list) -> list:
    max_vistas = max(tema["Vistas"] for tema in temas)
    return [tema for tema in temas if tema["Vistas"] == max_vistas]

def calcular_minima_reproduccion(temas: list) -> list:
    min_vistas = min(tema["Vistas"] for tema in temas)
    return [tema for tema in temas if tema["Vistas"] == min_vistas]

def buscar_codigo(temas: list):
    codigo = input("Ingrese el código del video: ").strip()
    for tema in temas:
        if tema["Codigo"] == codigo:
            print("\nDatos del video:")
            print(tema)
            return
    print("\nCódigo no encontrado.")

def listar_colaboraciones(temas: list):
    colaborador = input("Ingrese el nombre del colaborador: ").strip().lower()
    encontrados = [tema for tema in temas if colaborador in [c.lower() for c in tema["Colaboradores"]]]
    if encontrados:
        print(f"\nTemas de {colaborador.capitalize()}:")
        for tema in encontrados:
            print(f"- {tema['Tema']} | Fecha: {tema['Fecha Lanzamiento'].strftime('%Y-%m-%d')}")
    else:
        print("\nNo se encontraron colaboraciones.")

def listar_mes(temas: list):
    mes = int(input("Ingrese el mes (1-12): "))
    temas_mes = [tema for tema in temas if tema["Fecha Lanzamiento"].month == mes]
    if temas_mes:
        print(f"\nTemas lanzados en el mes {mes}:")
        for tema in temas_mes:
            print(f"- {tema['Tema']} | Fecha: {tema['Fecha Lanzamiento'].strftime('%Y-%m-%d')}")
    else:
        print(f"\nNo hay temas lanzados en el mes {mes}.")

# Menú principal
def menu():
    temas_normalizados = None
    while True:
        print("\n--- Menú de opciones ---")
        print("A. Normalizar datos")
        print("B. Mostrar temas")
        print("C. Ordenar temas por duración")
        print("D. Calcular promedio de vistas")
        print("E. Mostrar videos con máxima reproducción")
        print("F. Mostrar videos con mínima reproducción")
        print("G. Buscar por código")
        print("H. Listar por colaborador")
        print("I. Listar por mes")
        print("J. Salir")
        opcion = input("Seleccione una opción: ").upper()

        if opcion == "A":
            temas_normalizados = normalizar_datos(temas)
            print("\nDatos normalizados correctamente.")
        elif opcion in "BCDEFGHI":
            if temas_normalizados is None:
                print("\nPrimero debe normalizar los datos (opción A).")
            else:
                if opcion == "B":
                    mostrar_temas(temas_normalizados)
                elif opcion == "C":
                    temas_ordenados = ordenar_temas(temas_normalizados)
                    mostrar_temas(temas_ordenados)
                elif opcion == "D":
                    promedio = calcular_promedio_visitas(temas_normalizados)
                    print(f"\nPromedio de vistas: {promedio:.2f} millones")
                elif opcion == "E":
                    maximos = calcular_maxima_reproduccion(temas_normalizados)
                    print("\nVideos con máxima reproducción:")
                    for tema in maximos:
                        print(f"- {tema['Tema']} | Vistas: {tema['Vistas']}")
                elif opcion == "F":
                    minimos = calcular_minima_reproduccion(temas_normalizados)
                    print("\nVideos con mínima reproducción:")
                    for tema in minimos:
                        print(f"- {tema['Tema']} | Vistas: {tema['Vistas']}")
                elif opcion == "G":
                    buscar_codigo(temas_normalizados)
                elif opcion == "H":
                    listar_colaboraciones(temas_normalizados)
                elif opcion == "I":
                    listar_mes(temas_normalizados)
        elif opcion == "J":
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.")

# Ejecutar el menú
menu()