import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import pickle
import re
import os
import heapq
from collections import defaultdict

from Ficheros import *
from ConfigGeneral import *
from Genetico import *

def buscaTconvergencia(records, Tconvergencia):
    """
    Función para buscar el índice de la primera coincidencia de un valor en una lista de listas. Sirve para encontrar la iteración de convergencia del algoritmo genético.

    Args:
        records (array): Lista de listas con los valores de fitness de cada repetición.
        Tconvergencia (array): Lista donde se almacenarán los índices de convergencia.
    """    
    # Bucle para iterar sobre cada lista en records
    for lista in records:
        ultimo_valor = lista[-1]
        indice_primera_coincidencia = None  # Inicializamos con None para casos donde no hay coincidencias
        # Buscar el primer índice donde el valor coincide con el último valor de la lista
        for i, valor in enumerate(lista):
            if valor == ultimo_valor:
                indice_primera_coincidencia = i
                break  # Romper el bucle una vez encontrada la primera coincidencia

        # Agregar el resultado a Tconvergencia
        Tconvergencia.append(indice_primera_coincidencia)

def ObtenerDatos(resultados, NumIteraciones, RepsEstadistica):
    """
    Función para obtener los datos de los experimentos con el algoritmo genético y almacenarlos en una lista.

    Args:
        resultados (array): Lista donde se almacenarán los resultados.
        NumIteraciones (int): Número de iteraciones del algoritmo genético.
        RepsEstadistica (int): Número de repeticiones para realizar la estadística.
    """    
    contador = 0
    for Spadres in range(2):
        Super = 0 # Supervivientes Mixtos
        for Mutacion in range(2):
            for Cruce in range(2):
                for archivoD, archivoF in zip(FicherosD, FicherosF):
                    for NumPob in range(50, 200, 50):
                        for pm in np.arange(0.15, 0.35, 0.05):
                                records = []
                                Tconvergencia = []
                                for _ in range(RepsEstadistica):
                                    x = GeneralConfig(Spadres, Super, Mutacion, Cruce, archivoD, archivoF, NumPob, int(NumPob*0.5), pm)
                                    records.append(genetico_QAP(x.NumPob, x.NumPadres, x.pm, NumIteraciones, x.MatrizD, x.MatrizF, x.Spadres, x.Supervivientes, x.Mutacion, x.Cruce, rtop = x.ratio))
                                x.avg_min = [sum(column) / len(column) for column in zip(*records)]
                                buscaTconvergencia(records, Tconvergencia)
                                x.avg_Niter = sum(Tconvergencia)/len(Tconvergencia)
                                
                                resultados.append(x)
                                contador += 1
                                print(contador)
                                
def datos_para_practicar(resultados, NumIteraciones, RepsEstadistica,  ficheroD, ficheroF):
    """
    Función análoga a ObtenerDatos, pero se le pasa el nombre de los ficheros de distancia y flujo en lugar de recorrer

    Args:
        resultados (array): Lista donde se almacenarán los resultados.
        NumIteraciones (int): Número de iteraciones del algoritmo genético.
        RepsEstadistica (int): Número de repeticiones para realizar la estadística.
        ficheroD (string): Fichero de matriz de distancias.
        ficheroF (string): Ficher de matriz de flujos.
    
    Returns:
        array: Lista con los errores estándar de la media para cada repetición.
    """    
    print('Comenzamos...')
    records = []
    Tconvergencia = []
    for i in range(RepsEstadistica):
        x = GeneralConfig(Spadres = 1, Super = 0, Mutacion = 1, Cruce = 1, MatrizD = ficheroD, MatrizF = ficheroF, NumPob = 700, NumPadres = int(700*0.5), pm = 0.20, ratio = 0.70)
        records.append(genetico_QAP(x.NumPob, x.NumPadres, x.pm, NumIteraciones, x.MatrizD, x.MatrizF, x.Spadres, x.Supervivientes, x.Mutacion, x.Cruce, rtop = x.ratio))
        print(i)
    
    x.avg_min = [sum(column) / len(column) for column in zip(*records)]
    standard_errors = [np.std(column) / np.sqrt(len(column)) for column in zip(*records)]
    buscaTconvergencia(records, Tconvergencia)
    x.avg_Niter = sum(Tconvergencia)/len(Tconvergencia)                               
    
    resultados.append(x)
    return(standard_errors)
                                                


def ObtenerEvolucion2(comparacion, ruta_archivo_datos, ruta_guardar_imagenes):
    """
    Función para obtener la evolución de la función fitness y comparar para los distintos valores posibles de ese parámetro. Finalmente guardar las gráficas en un directorio.

    Args:
        comparacion (string): Parámetro a comparar.
        ruta_archivo_datos (string): Ruta donde está guardado el archivo de datos con los resultadoos.
        ruta_guardar_imagenes (string): Ruta donde se desea guardar las imágenes generadas.
    """  
    with open(ruta_archivo_datos, 'rb') as f:
        my_loaded_list = pickle.load(f)

    # Organizar los datos por valor de comparación y por ejemplo
    data_dict = {}
    for item in my_loaded_list:
        param_value = getattr(item, comparacion)
        ejemplo = item.MatrizD
        match = re.search(r'Ejemplo_(\d+)_D\.txt', ejemplo)
        if match:
            numero_ejemplo = match.group(1)
            ruta_especifica = os.path.join(ruta_guardar_imagenes, f'Ejemplo_NumPob_{numero_ejemplo}/')

            if ruta_especifica not in data_dict:
                data_dict[ruta_especifica] = {}
            if param_value not in data_dict[ruta_especifica]:
                data_dict[ruta_especifica][param_value] = []

            data_dict[ruta_especifica][param_value].append(item.avg_min)

    # Crear y guardar gráficos para cada ejemplo y cada valor de comparación
    for ruta, params in data_dict.items():
        plt.figure()
        # Definir colores específicos en el orden solicitado
        # color_palette = np.array(['#67ADF9', '#FA86EC', '#FFFD6B', '#4A493C'])
        labels_added = set()  # Conjunto para controlar las etiquetas añadidas a la leyenda

        # Ordenar los parámetros de mayor a menor antes de graficar
        sorted_params = sorted(params.keys(), reverse=False, key=lambda x: float(x))

        # Mapas para las etiquetas personalizadas
        spadres_labels = {
            0: 'Aleatoria',
            1: 'Por torneo'
        }

        mutacion_labels = {
            0: 'Por inversión',
            1: 'Por intercambio'
        }

        cruce_labels = {
            0: 'De orden',
            1: 'Parcialmente mapeado'
        }

        for param_value in sorted_params:
        #     color = color_palette[sorted_params.index(param_value) % len(color_palette)]
            series = params[param_value]
            
            # Asignar el formato correcto según el parámetro 'comparacion'
            if comparacion in ['pm', 'ratio']:
                label = f'{param_value:.2f}'
            elif comparacion == 'NumPob':
                label = f'{int(param_value)}'
            elif comparacion == 'Spadres':
                label = spadres_labels.get(param_value, str(param_value))
            elif comparacion == 'Mutacion':
                label = mutacion_labels.get(param_value, str(param_value))
            elif comparacion == 'Cruce':
                label = cruce_labels.get(param_value, str(param_value))
            else:
                label = str(param_value)

            for avg_min in series:
                if param_value not in labels_added:
                    plt.plot(avg_min, label=label)#, color=color)
                    labels_added.add(param_value)
                else:
                    plt.plot(avg_min)#, color=color)

        plt.title('')
        plt.xlabel('Número de iteración')
        plt.ylabel('Fitness mínimo medio')
        plt.legend(title=comparacion)
        plt.tight_layout()

        # Guardar la gráfica
        archivo_grafico = os.path.join(ruta, f'Evolucion_{comparacion}_completa.pdf')
        plt.savefig(archivo_grafico)
        plt.close()
        print(f'Gráfico completo guardado en {archivo_grafico}')


def ObtenerEvolucion3(comparacion, valor_parametro, ruta_archivo_datos, ruta_guardar_imagenes):
    """
    Función para obtener la evolución de la función fitness por colores para las 8 distintas combinaciones de tipos de algoritmo
    (Spadres, Mutación, Cruce) para un valor específico de un parámetro de comparación. Finalmente guardar las gráficas en un directorio.

    Args:
        comparacion (string): Parámetro a comparar.
        valor_parametro (int): Valor específico del parámetro a comparar.
        ruta_archivo_datos (string): Ruta donde está guardado el archivo de datos con los resultadoos.
        ruta_guardar_imagenes (string): Ruta donde se desea guardar las imágenes generadas.
    """    
    with open(ruta_archivo_datos, 'rb') as f:
        my_loaded_list = pickle.load(f)

    # Definir la paleta de colores
    color_palette = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'grey', 'pink']

    # Organizar los datos por ejemplo y parámetros
    data_dict = {}
    color_used = {}  # Diccionario para controlar los colores usados y sus etiquetas

    for item in my_loaded_list:
        if getattr(item, comparacion) == valor_parametro:
            ejemplo = item.MatrizD
            match = re.search(r'Ejemplo_(\d+)_D\.txt', ejemplo)
            if match:
                numero_ejemplo = match.group(1)
                ruta_especifica = os.path.join(ruta_guardar_imagenes, f'Ejemplo_{numero_ejemplo}/')
                param_key = (item.Spadres, item.Mutacion, item.Cruce)

                if ruta_especifica not in data_dict:
                    data_dict[ruta_especifica] = {}
                if param_key not in data_dict[ruta_especifica]:
                    data_dict[ruta_especifica][param_key] = []

                data_dict[ruta_especifica][param_key].append(item.avg_min)

    # Crear y guardar gráficos para cada ejemplo
    for ruta, params in data_dict.items():
        plt.figure()
        sorted_params = sorted(params.keys())  # Ordenar las claves para un color consistente
        color_map = {key: color_palette[i % len(color_palette)] for i, key in enumerate(sorted_params)}
        
        # Crear una lista de etiquetas únicas para cada color
        unique_labels = []

        for param_key in sorted_params:
            series = params[param_key]
            color = color_map[param_key]
            
            # Asignar una etiqueta única a cada combinación de parámetros
            if color not in unique_labels:
                label = f'({param_key[0]}, {param_key[1]}, {param_key[2]})'
                unique_labels.append(color)
            else:
                label = None
            
            contador = 0
            for avg_min in series:
                if contador == 0:
                    plt.plot(avg_min, label=label, color=color)
                else:
                    plt.plot(avg_min, color=color)
                contador += 1
            
            

    plt.legend(title='(Spadres, Mutación, Cruce)')

    plt.title(f'{comparacion} = {valor_parametro}')
    plt.xlabel('Número de iteración')
    plt.ylabel('Fitness mínimo medio')
    plt.tight_layout()

    archivo_grafico = os.path.join(ruta, f'Evolucion_{comparacion}_{valor_parametro}_completa.pdf')
    plt.savefig(archivo_grafico)
    plt.close()
    print(f'Gráfico completo guardado en {archivo_grafico}')


def ObtenerComparacion(comparacion, ruta_archivo_datos, ruta_guardar_imagenes):
    """
    Función para obtener 2 gráficas: la primera es la comparación de la media de la última iteración y la segunda es la media de la 
    iteración de convergencia. En ambos casos se obtienen en función de un parámetro de comparación y se guardar las 2 gráficas en un directorio.

    Args:
        comparacion (string): Parámetro a comparar.
        ruta_archivo_datos (string): Ruta donde está guardado el archivo de datos con los resultadoos.
        ruta_guardar_imagenes (string): Ruta donde se desea guardar las imágenes generadas.
    """     
    with open(ruta_archivo_datos, 'rb') as f:
        my_loaded_list = pickle.load(f)

    # Organizar los datos por archivo MatrizD
    directorio_dict = {}
    param_color_mapping = {}  # Para mapear cada parámetro a un color específico
    unique_params = set()  # Conjunto para recolectar valores únicos de parámetros

    for item in my_loaded_list:
        param_value = getattr(item, comparacion)
        unique_params.add(param_value)  # Añadir valor a conjunto de únicos
        matrizd = item.MatrizD
        match = re.search(r'Ejemplo_(\d+)_D\.txt', matrizd)
        if match:
            numero_ejemplo = match.group(1)
            ruta_especifica = os.path.join(ruta_guardar_imagenes, f'Ejemplo_NumPob_{numero_ejemplo}')
            if ruta_especifica not in directorio_dict:
                directorio_dict[ruta_especifica] = {'params': [], 'avg_min_last': [], 'avg_Niter': []}
            
            directorio_dict[ruta_especifica]['params'].append(param_value)
            directorio_dict[ruta_especifica]['avg_min_last'].append(item.avg_min[-1] if item.avg_min else None)
            directorio_dict[ruta_especifica]['avg_Niter'].append(item.avg_Niter if item.avg_Niter else None)

    # Asignar colores a cada parámetro único
    unique_params = sorted(list(unique_params))  # Convertir conjunto a lista y ordenar
    # color_palette = np.array(['#67ADF9', '#FA86EC', '#FFFD6B', '#4A493C'])
    # if len(unique_params) > len(color_palette):
    #     raise ValueError("No hay suficientes colores para todos los parámetros únicos.")

    # for i, param in enumerate(unique_params):
    #     param_color_mapping[param] = color_palette[i % len(color_palette)]

    # Mapas para las etiquetas personalizadas
    spadres_labels = {
        0: 'Aleatoria',
        1: 'Torneo'
    }

    mutacion_labels = {
        0: 'Inversión',
        1: 'Intercambio'
    }

    cruce_labels = {
        0: 'Orden',
        1: 'P. mapped'
    }

    # Crear dos gráficos separados por cada directorio
    for ruta_especifica, data in directorio_dict.items():
        # Gráfico para avg_min_last
        plt.figure()
        for param, avg_min in zip(data['params'], data['avg_min_last']):
            plt.scatter(param, avg_min, color='darkblue')

        # Configurar el eje X
        if comparacion in ['Spadres', 'Mutacion', 'Cruce']:
            if comparacion == 'Spadres':
                labels = spadres_labels
            elif comparacion == 'Mutacion':
                labels = mutacion_labels
            elif comparacion == 'Cruce':
                labels = cruce_labels

            plt.xticks(ticks=list(labels.keys()), labels=list(labels.values()))

        plt.title('')
        plt.xlabel(comparacion)
        plt.ylabel('Fitness mínimo medio final')
        plt.tight_layout()
        os.makedirs(ruta_especifica, exist_ok=True)
        ruta_completa_min = os.path.join(ruta_especifica, f'{comparacion}_minimo.pdf')
        plt.savefig(ruta_completa_min)
        plt.close()

        # Gráfico para avg_Niter
        plt.figure()
        for param, avg_niter in zip(data['params'], data['avg_Niter']):
            plt.scatter(param, avg_niter, color='darkblue')

        # Configurar el eje X
        if comparacion in ['Spadres', 'Mutacion', 'Cruce']:
            plt.xticks(ticks=list(labels.keys()), labels=list(labels.values()))

        plt.title('')
        plt.xlabel(comparacion)
        plt.ylabel('Iteración de convergencia media')
        plt.tight_layout()
        ruta_completa_conv = os.path.join(ruta_especifica, f'{comparacion}_convergencia.pdf')
        plt.savefig(ruta_completa_conv)
        plt.close()



def group_objects_by_attribute(my_loaded_list, attribute):
    """
    Función para agrupar objetos por el valor de un atributo específico.
    
    Args:
        my_loaded_list (string): Archivo de datos con los resultados de los experimentos.
        attribute (string): Atributo por el que se desea agrupar los objetos.

    Returns:
        disctionary: Diccionario con los objetos agrupados por el valor del atributo.
    """    
    objects_grouped_by_attribute = defaultdict(list)

    for obj in my_loaded_list:
        objects_grouped_by_attribute[getattr(obj, attribute)].append(obj)

    return objects_grouped_by_attribute

def MostrarMinimos(my_loaded_list, attribute):
    """
    Función para mostrar los 10 objetos con los valores más bajos de la última iteración de la función fitness, 
    agrupados por un atributo específico.

    Args:
        my_loaded_list (string): Archivo de datos con los resultados de los experimentos.
        attribute (string): Atributo por el que se desea agrupar los objetos.
    """    
    objects_grouped_by_attribute = group_objects_by_attribute(my_loaded_list, attribute)

    # Iterar sobre los grupos y mostrar los 10 objetos con los valores más bajos de avg_min[-1]
    for attribute_value, my_loaded_list in objects_grouped_by_attribute.items():
        print(f"\nObjects with {attribute_value} for {attribute}:")
        print("Output format: (Spadres, Mutacion, Cruce, NumPob, pm, ratio, avg_Niter, avg_min[-1])")
        # Crear una lista de tuplas (avg_min[-1], object) para cada objeto en el grupo
        value_object_pairs = [(obj.avg_min[-1], obj) for obj in my_loaded_list]

        # Obtener los 10 pares con los valores más bajos
        ten_smallest_value_object_pairs = heapq.nsmallest(10, value_object_pairs)

        # Obtener solo los objetos de los pares
        ten_objects_with_smallest_values = [pair[1] for pair in ten_smallest_value_object_pairs]

        # Imprimimos los objetos
        contador = 1
        for i in ten_objects_with_smallest_values:
            print('\n')
            print(f"Dato número: {contador}")
            print(f"({i.Spadres}, {i.Mutacion}, {i.Cruce}, {i.NumPob}, {i.pm:.2f}, {i.ratio}, {i.avg_Niter}, {i.avg_min[-1]})")
            contador += 1


