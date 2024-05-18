import pickle

from Ficheros import *
from ConfigGeneral import *
from Genetico import *
from Utils import *
import statistics
import time




# RepsEstadistica = 20
# NumIteraciones = 500

# Super = 0 
# Spadres = 1
# Mutacion = 1
# Cruce = 1   

# archivoD = "Ejemplo_3_D.txt"
# archivoF = "Ejemplo_3_F.txt"
# NumPob = 1000
# pm = 0.2
# ratio = 0.7


# records = []
# Tconvergencia = []
# resultados = []
# start_time = time.time()

# print('Comenzamos...')
# for i in range(RepsEstadistica):
#     x = GeneralConfig(Spadres, Super, Mutacion, Cruce, archivoD, archivoF, NumPob, int(NumPob*0.5), pm, ratio)
#     records.append(genetico_QAP(x.NumPob, x.NumPadres, x.pm, NumIteraciones, x.MatrizD, x.MatrizF, x.Spadres, x.Supervivientes, x.Mutacion, x.Cruce, rtop = x.ratio))
#     print(i)

# x.avg_min = [sum(column) / len(column) for column in zip(*records)]
# buscaTconvergencia(records, Tconvergencia)
# x.avg_Niter = sum(Tconvergencia)/len(Tconvergencia)                               
# resultados.append(x)


# # To export the list to a file, we first open a file in binary write mode
# with open('resultados.pkl', 'wb') as f:
#     # Then we use pickle.dump() to dump the list into the file
#     pickle.dump(resultados, f)




# with open('DatosEjemplo2_NumPobIteration.pkl', 'rb') as f:
#     my_loaded_list = pickle.load(f)

# NConvergencia = []
# Minimos = []

# for i in range(len(my_loaded_list)):
#     print('\n')
#     print(f"Dato número: {i}")
#     print(f"Selección de padres: {my_loaded_list[i].Spadres}") 
#     print(f"Elección de supervivientes: {my_loaded_list[i].Supervivientes}") 
#     print(f"Tipo de mutación: {my_loaded_list[i].Mutacion}") 
#     print(f"Tipo de cruce: {my_loaded_list[i].Cruce}") 
#     print(f"Fichero de distancias: {my_loaded_list[i].MatrizD}") 
#     print(f"Fichero de flujos: {my_loaded_list[i].MatrizF}") 
#     print(f"Población: {my_loaded_list[i].NumPob}") 
#     print(f"Número de padres: {my_loaded_list[i].NumPadres}") 
#     print(f"Probabilidad de mutación: {my_loaded_list[i].pm:.2f}")
#     print(f" Iteración media de convergencia: {my_loaded_list[i].avg_Niter}")
#     print(f"Lista de valores medios minimos a cada paso: \n {my_loaded_list[i].avg_min}")
#     print('\n')
#     NConvergencia.append(my_loaded_list[i].avg_Niter)
#     Minimos.append(my_loaded_list[i].avg_min[-1])
    
# print(f"Iteración media de convergencia: {statistics.mean(NConvergencia):.2f} +- {statistics.stdev(NConvergencia):.2f}")
# print(f"Valor mínimo medio: {statistics.mean(Minimos):.2f} +- {statistics.stdev(Minimos):.2f}")    

# # End time
# end_time = time.time()
# # Time taken
# time_taken = end_time - start_time
# print(f"The program took {time_taken} seconds to run.")
    



# ObtenerEvolucion('DatosParaPruebas.pkl', 'Gráficas/')
# ObtenerComparacion('pm', 'DatosParaPruebas.pkl', 'Gráficas/')

# MostrarMinimos(my_loaded_list, 'Spadres')
# ObtenerEvolucion2('Spadres', 'DatosEjemplo3.pkl', 'Gráficas/') 
# ObtenerEvolucion2('Mutacion', 'DatosEjemplo3.pkl', 'Gráficas/') 
# ObtenerEvolucion2('Cruce', 'DatosEjemplo3.pkl', 'Gráficas/') 
# ObtenerEvolucion2('NumPob', 'DatosEjemplo3.pkl', 'Gráficas/') 
# ObtenerEvolucion2('pm', 'DatosEjemplo3.pkl', 'Gráficas/') 
# ObtenerEvolucion2('ratio', 'DatosEjemplo3.pkl', 'Gráficas/') 

# ObtenerEvolucion3('NumPob', 50, 'DatosEjemplo1.pkl', 'Gráficas/')
# ObtenerEvolucion3('NumPob', 50, 'DatosEjemplo2.pkl', 'Gráficas/')
# ObtenerEvolucion3('NumPob', 50, 'DatosEjemplo3.pkl', 'Gráficas/')
# ObtenerEvolucion3('NumPob', 100, 'DatosEjemplo1.pkl', 'Gráficas/')
# ObtenerEvolucion3('NumPob', 100, 'DatosEjemplo2.pkl', 'Gráficas/')
# ObtenerEvolucion3('NumPob', 100, 'DatosEjemplo3.pkl', 'Gráficas/')
# ObtenerEvolucion3('NumPob', 150, 'DatosEjemplo1.pkl', 'Gráficas/')
# ObtenerEvolucion3('NumPob', 150, 'DatosEjemplo2.pkl', 'Gráficas/')
# ObtenerEvolucion3('NumPob', 150, 'DatosEjemplo3.pkl', 'Gráficas/')

# ObtenerEvolucion2('NumPob', 'DatosEjemplo1_NumPobIteration.pkl', 'Gráficas/') 
# ObtenerComparacion('NumPob', 'DatosEjemplo1_NumPobIteration.pkl', 'Gráficas/') 

# ObtenerEvolucion2('NumPob', 'DatosEjemplo2_NumPobIteration.pkl', 'Gráficas/') 
# ObtenerComparacion('NumPob', 'DatosEjemplo2_NumPobIteration.pkl', 'Gráficas/') 

# ObtenerEvolucion2('NumPob', 'DatosEjemplo3_NumPobIteration.pkl', 'Gráficas/') 
# ObtenerComparacion('NumPob', 'DatosEjemplo3_NumPobIteration.pkl', 'Gráficas/') 

# ObtenerComparacion('Spadres', 'DatosEjemplo3.pkl', 'Gráficas/')
# ObtenerComparacion('Mutacion', 'DatosEjemplo3.pkl', 'Gráficas/') 
# ObtenerComparacion('Cruce', 'DatosEjemplo3.pkl', 'Gráficas/') 
# ObtenerComparacion('NumPob', 'DatosEjemplo3.pkl', 'Gráficas/') 
# ObtenerComparacion('pm', 'DatosEjemplo3.pkl', 'Gráficas/') 
# ObtenerComparacion('ratio', 'DatosEjemplo3.pkl', 'Gráficas/') 
