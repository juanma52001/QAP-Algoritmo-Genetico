# Para generar las matrices de distancias y de flujos
import numpy as np

def generar_matriz_simetrica_enteros(N, cota_min, cota_max):
    """
    Genera una matriz simétrica de enteros aleatorios en el rango [cota_min, cota_max], con ceros en la diagonal.

    Args:
        N (int): Dimensión de la matriz cuadrada.
        cota_min (int): Valor mínimo de los enteros de la matriz.
        cota_max (int): Valor máximo de los enteros de la matriz.

    Returns:
        int matrix: Matriz generada.
    """    
    # Generamos una matriz aleatoria de enteros
    matriz = np.random.randint(cota_min, cota_max+1, size=(N, N))
    # La hacemos simétrica
    matriz = (matriz + matriz.T) // 2
    # Fijamos la diagonal a 0
    np.fill_diagonal(matriz, 0)
    return matriz

def guardar_matriz_en_txt(matriz, nombre_archivo):
    """
    Guarda una matriz en un archivo de texto.

    Args:
        matriz (matrix): Matriz a guardar.
        nombre_archivo (string): Nombre del archivo de texto.
    """    
    with open(nombre_archivo, 'w') as f:
        for fila in matriz:
            f.write(' '.join(map(str, fila)) + '\n')


# Guardamos las matrices en archivos de texto. Queremos varios ejemplos (3 en concreto)

# Ejemplo 1
matriz1D = generar_matriz_simetrica_enteros(20, 1, 25)
matriz1F = generar_matriz_simetrica_enteros(20, 1, 30)
guardar_matriz_en_txt(matriz1D, f'Ejemplo_1_D.txt')
guardar_matriz_en_txt(matriz1F, f'Ejemplo_1_F.txt')

# Ejemplo 2
matriz2D = generar_matriz_simetrica_enteros(40, 1, 50)
matriz2F = generar_matriz_simetrica_enteros(40, 10, 70)
guardar_matriz_en_txt(matriz2D, f'Ejemplo_2_D.txt')
guardar_matriz_en_txt(matriz2F, f'Ejemplo_2_F.txt')

# Ejemplo 3
matriz3D = generar_matriz_simetrica_enteros(60, 25, 100)
matriz3F = generar_matriz_simetrica_enteros(60, 30, 200)
guardar_matriz_en_txt(matriz3D, f'Ejemplo_3_D.txt')
guardar_matriz_en_txt(matriz3F, f'Ejemplo_3_F.txt')