import pandas as pd
import os
from random import choice, random
from datetime import datetime, timedelta

# ==============================================================================

# Caso 1: Estructura de Datos para el Sistema de Gestión de Animales
class Animal:
    def __init__(self, id_chip, nombre, especie, raza, edad, peso,
                 fecha_ingreso, estado_salud, adoptado=False):
        self.id_chip = id_chip
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.fecha_ingreso = fecha_ingreso
        self.estado_salud = estado_salud
        self.adoptado = adoptado
        self.historial_medico = []

# Caso 2: Estructuras de Datos para el Sistema de Adopciones y Seguimiento
class Adoptante:
    def __init__(self, id_adoptante, nombre, edad, ingresos, tipo_vivienda,
                 experiencia_animales, preferencias):
        self.id_adoptante = id_adoptante
        self.nombre = nombre
        self.edad = edad
        self.ingresos = ingresos
        self.tipo_vivienda = tipo_vivienda
        self.experiencia_animales = experiencia_animales
        self.preferencias = preferencias
        self.historial_adopciones = []

class Adopcion:
    def __init__(self, id_adopcion, id_animal, id_adoptante, fecha_adopcion):
        self.id_adopcion = id_adopcion
        self.id_animal = id_animal
        self.id_adoptante = id_adoptante
        self.fecha_adopcion = fecha_adopcion
        self.seguimientos = []

# ==============================================================================

def load_datasets():
    datasets_folder = "datasets"
    animals_df = None
    adoptantes_df = None
    adopciones_df = None

    # Cargar el dataset de animales
    try:
        animals_df = pd.read_csv(os.path.join(datasets_folder, "refugio_animales.csv"))
        print(f"Total de animales: {len(animals_df)}.\n")
    except FileNotFoundError:
        print(f"Error: El archivo 'refugio_animales.csv' no se encontró en '{datasets_folder}'. Asegúrese de que la carpeta y el archivo existen.")
    except Exception as e:
        print(f"Ocurrió un error al cargar 'refugio_animales.csv': {e}")

    # Cargar el dataset de adoptantes
    try:
        adoptantes_df = pd.read_csv(os.path.join(datasets_folder, "adoptantes.csv"))
        print(f"Total de adoptantes: {len(adoptantes_df)}.\n")
    except FileNotFoundError:
        print(f"Error: El archivo 'adoptantes.csv' no se encontró en '{datasets_folder}'. Asegúrese de que la carpeta y el archivo existen.")
    except Exception as e:
        print(f"Ocurrió un error al cargar 'adoptantes.csv': {e}")

    # Cargar el dataset de adopciones
    try:
        adopciones_df = pd.read_csv(os.path.join(datasets_folder, "adopciones.csv"))
        print(f"Total de adopciones: {len(adopciones_df)}.\n")
    except FileNotFoundError:
        print(f"Error: El archivo 'adopciones.csv' no se encontró en '{datasets_folder}'. Asegúrese de que la carpeta y el archivo existen.")
    except Exception as e:
        print(f"Ocurrió un error al cargar 'adopciones.csv': {e}")

    return animals_df, adoptantes_df, adopciones_df

# ==============================================================================

def show_case_1_info(animals_df):
    print("\n" + "="*70)
    print("                 INFORMACIÓN DEL CASO 1: REGISTRO DE ANIMALES")
    print("="*70)
    print("Objetivo: Administrar la información de todos los animales del refugio. ")
    print("\nEjemplo de datos cargados (primeros 5 animales):")
    if animals_df is not None:
        print(animals_df.head().to_string())
    else:
        print("No se pudieron cargar los datos de animales.")

def show_case_2_info(adoptantes_df, adopciones_df):
    print("\n" + "="*70)
    print("             INFORMACIÓN DEL CASO 2: ADOPCIONES Y SEGUIMIENTO")
    print("="*70)
    print("Objetivo: Administrar de forma efectiva el proceso de adopción y el seguimiento posterior de los animales, asegurando el mejor hogar para cada uno. ")
    print("\nEjemplo de datos cargados (primeros 5 adoptantes):")
    if adoptantes_df is not None:
        print(adoptantes_df.head().to_string())
    else:
        print("No se pudieron cargar los datos de adoptantes.")
    print("\nEjemplo de datos cargados (primeras 5 adopciones):")
    if adopciones_df is not None:
        print(adopciones_df.head().to_string())
    else:
        print("No se pudieron cargar los datos de adopciones.")

def show_general_info(animals_df, adoptantes_df, adopciones_df):
    print("\n" + "="*70)
    print("               RESUMEN GENERAL DE ALGORITMOS Y CASOS")
    print("="*70)
    print("Este trabajo aborda los algoritmos de búsqueda y ordenamiento, pilares fundamentales en la programación. ")
    print("Se analizan teóricamente e implementan en Python para evaluar su rendimiento. ")
    print("\nFundamentos de Búsqueda:")
    print("- Búsqueda Lineal: Sencilla, O(n), útil en listas pequeñas o no ordenadas. ")
    print("- Búsqueda Binaria: Más eficiente, O(log n), requiere lista ordenada, ideal para listas grandes. ")
    print("- Hashing: Acceso directo en tiempo constante O(1) si no hay colisiones, base de diccionarios en Python. ")
    print("\nFundamentos de Ordenamiento:")
    print("- Bubble Sort: Intuitivo pero ineficiente en listas grandes, O(n²). ")
    print("- Quick Sort: Muy eficiente en promedio (O(n log n)), pero puede tener peor rendimiento con pivote mal elegido. ")
    print("- Merge Sort: Rendimiento garantizado de O(n log n) en todos los casos, estable, pero consume más memoria. ")
    print("\nAnálisis de Resultados Clave:")
    print("- QuickSort superó a los demás en casi todos los escenarios. ")
    print("- MergeSort fue constante y predecible, ideal cuando se requiere estabilidad. ")
    print("- BubbleSort fue claramente el más lento. ")
    print("- La búsqueda binaria fue muy rápida solo con datos ordenados. ")
    print("\nRecomendaciones:")
    print("- Usar QuickSort o MergeSort para grandes volúmenes de datos. ")
    print("- Evitar Bubble Sort excepto con fines didácticos. ")
    print("- Implementar búsqueda binaria solo si los datos están ordenados. ")
    print("- Evaluar el uso de hash para acceso rápido en bases de datos grandes. ")
    print("\nVisualización de Datos (primeras 5 filas de cada dataset):")
    if animals_df is not None:
        print("\nDataset 'refugio_animales.csv':")
        print(animals_df.head().to_string())
    if adoptantes_df is not None:
        print("\nDataset 'adoptantes.csv':")
        print(adoptantes_df.head().to_string())
    if adopciones_df is not None:
        print("\nDataset 'adopciones.csv':")
        print(adopciones_df.head().to_string())
    print("\n" + "="*70 + "\n")

# ==============================================================================

if __name__ == "__main__":
    # Cargar o generar los datasets
    animals_df, adoptantes_df, adopciones_df = load_datasets()

    while True:
        print("\n" + "="*40)
        print("         MENÚ DE INFORMACIÓN")
        print("="*40)
        print("1. Información del Caso 1: Gestión de Animales")
        print("2. Información del Caso 2: Adopciones y Seguimiento")
        print("3. Resumen General de Algoritmos y Casos")
        print("4. Salir")
        print("="*40)

        choice = input("Ingrese su opción (1-4): ")

        if choice == '1':
            if animals_df is not None:
                show_case_1_info(animals_df)
            else:
                print("\nError: No se pudieron cargar los datos para el Caso 1. Verifique los archivos CSV.")
        elif choice == '2':
            if adoptantes_df is not None and adopciones_df is not None:
                show_case_2_info(adoptantes_df, adopciones_df)
            else:
                print("\nError: No se pudieron cargar los datos para el Caso 2. Verifique los archivos CSV.")
        elif choice == '3':
            show_general_info(animals_df, adoptantes_df, adopciones_df)
        elif choice == '4':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número entre 1 y 4.")