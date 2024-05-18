from Utils import *
import pickle
import time


if __name__ == "_main_":
    # Para controlar el tiempo de compilación
    start_time = time.time()
    
    # Creamos el objeto que contiene los distintos parámetros, para hacer estadística
    NumIteraciones = 500
    RepsEstadistica = 20
    
    resultados = []
    errores = []
    errores = datos_para_practicar(resultados, NumIteraciones, RepsEstadistica, 'Ejemplo_1_D.txt', 'Ejemplo_1_F.txt')
    print(f"Valor mínimo medio para el ejemplo 1: {resultados[0].avg_min[-1]:.2f} +- {errores[-1]:.2f}")  
    resultados = []
    errores = []
    errores = datos_para_practicar(resultados, NumIteraciones, RepsEstadistica, 'Ejemplo_2_D.txt', 'Ejemplo_2_F.txt')
    print(f"Valor mínimo medio para el ejemplo 2: {resultados[0].avg_min[-1]:.2f} +- {errores[-1]:.2f}")  
    resultados = []
    errores = []
    errores = datos_para_practicar(resultados, NumIteraciones, RepsEstadistica, 'Ejemplo_3_D.txt', 'Ejemplo_3_F.txt')
    print(f"Valor mínimo medio para el ejemplo 3: {resultados[0].avg_min[-1]:.2f} +- {errores[-1]:.2f}")  
    
    end_time = time.time()
    time_taken = end_time - start_time
    print(f"Le ha costado {time_taken} segundos correr al programa.")
    