import numpy as np
import random

def evaluaFO(X, flujos, distancias):
    """
    Cálculo de la función objetivo para el QAP

    Args:
        X (int array): Permutación de las localizaciones.
        flujos (matrix): Matriz de flujos.
        distancias (matrix): Matriz de distancias.
    
    Returns:
        float: Valor de la función objetivo.
    """    
    N = len(X)
    fit = 0
    for i in range(N):
        for j in range(i+1, N): # Evitamos los terminos repetidos en la suma sumando solo en la mitad superior de la matriz
            fit += flujos[int(X[i]),int(X[j])]*distancias[i,j]
    return(fit)


def cruceO(individuo1, individuo2, N):
    """
    Cruce de orden para el algoritmo genético.

    Args:
        individuo1 (int array): Primer individuo a cruzar.
        individuo2 (int array): Segundo individuo a cruzar.
        N (int): Tamaño de la permutación.
    
    Returns:
        int matrix: Matriz con los descendientes.
    """    
    descendientes = np.zeros([N,2])
    descendientes = descendientes-1
  
    pos = sorted(random.sample(range(N),2))
    descendientes[pos[0]:pos[1]+1,0] = individuo1[pos[0]:pos[1]+1]
    descendientes[pos[0]:pos[1]+1,1] = individuo2[pos[0]:pos[1]+1]

    # Construyo descendiente 1  
    if (pos[1] < N-1):
        k = pos[1]+1
        for j in range(pos[1]+1,N):
            if (individuo2[j] not in descendientes[:,0]):
                descendientes[k,0] = individuo2[j]
                k = k+1
                if (k==N):
                    k = 0                   
        for j in range(pos[1]+1):
            if (individuo2[j] not in descendientes[:,0]):
                descendientes[k,0] = individuo2[j]
                k = k+1
                if (k==N):
                    k = 0                
    else:
        k = 0
        for j in range(pos[1]+1):
            if (individuo2[j] not in descendientes[:,0]):
                descendientes[k,0] = individuo2[j]
                k = k+1
                if (k==N):
                    k = 0

    # Construyo descendiente 2  
    if (pos[1] < N-1):
        k = pos[1]+1
        for j in range(pos[1]+1,N):
            if (individuo1[j] not in descendientes[:,1]):
                descendientes[k,1] = individuo1[j]
                k = k+1
                if (k==N):
                    k = 0                   
        for j in range(pos[1]+1):
            if (individuo1[j] not in descendientes[:,1]):
                descendientes[k,1] = individuo1[j]
                k = k+1
                if (k==N):
                    k = 0                
    else:
        k = 0
        for j in range(pos[1]+1):
            if (individuo1[j] not in descendientes[:,1]):
                descendientes[k,1] = individuo1[j]
                k = k+1
                if (k==N):
                    k = 0
                
    return(descendientes)



def crucePM(individuo1, individuo2, N):
    """
    Cruce parcialmente mapped para el algoritmo genético.

    Args:
        individuo1 (int array): Primer individuo a cruzar.
        individuo2 (int array): Segundo individuo a cruzar.
        N (int): Tamaño de la permutación.

    Returns:
        int matrix: Matriz con los descendientes.
    """    
    
    descendientes = np.zeros([N,2], dtype = float)
    descendientes = descendientes-1
    
    # Elijo la subcadena y copio los cachos (paso 1)
    pos = sorted(random.sample(range(N),2)) # Elijo 2 posiciones aleatorias, de menor a mayor ordenadas. Los puntos de la subcadena

    descendientes[pos[0]:pos[1]+1,0] = individuo1[pos[0]:pos[1]+1] # Copio en el primer descendiente la subcadena del individuo1
    descendientes[pos[0]:pos[1]+1,1] = individuo2[pos[0]:pos[1]+1] # Copio en el segundo descendiente la subcadena del individuo2

    # Construyo descendiente 1
    for i in range(pos[0], pos[1]+1):
        if individuo2[i] not in descendientes[pos[0]:pos[1]+1, 0]:
            for j, elemento in enumerate(individuo2):
                if elemento == individuo1[i]:
                    indice = j
                    break  # Termina el bucle al encontrar la primera coincidencia
            while indice in range(pos[0], pos[1]+1): # Cuando el índice es uno de los índices copiados, no nos sirve, elegimos nuevo indice
                for j, elemento in enumerate(individuo2):
                    if elemento == individuo1[indice]:
                        indice = j
                        break
            descendientes[indice, 0] = individuo2[i]
    # Tras acabar, copio los índices que sean -1 al valor que haya en individuo2
    for i in range(N):
        if descendientes[i, 0] == -1:
            descendientes[i, 0] = individuo2[i]

    # Construyo descendiente 2
    for i in range(pos[0], pos[1]+1):
        if individuo1[i] not in descendientes[pos[0]:pos[1]+1, 1]:
            for j, elemento in enumerate(individuo1):
                if elemento == individuo2[i]:
                    indice = j
                    break  # Termina el bucle al encontrar la primera coincidencia
            while indice in range(pos[0], pos[1]+1): # Cuando el índice es uno de los índices copiados, no nos sirve, elegimos nuevo indice
                for j, elemento in enumerate(individuo1):
                    if elemento == individuo2[indice]:
                        indice = j
                        break
            descendientes[indice, 1] = individuo1[i]
    # Tras acabar, copio los índices que sean -1 al valor que haya en individuo1

    for i in range(N):
        if descendientes[i, 1] == -1:
            descendientes[i, 1] = individuo1[i]

    return(descendientes)

def mutacionInter(hijos,pm,N):
    """
    Mutación por intercambio.

    Args:
        hijos (matrix): Matriz con los hijos a mutar.
        pm (float): Probabilidad de mutación.
        N (int): Tamaño de la permutación.
    
    Returns:
        int matrix: Matriz con los hijos mutados.
    """
    for i in range(2):
        a = np.random.uniform()
        if(a < pm):
            pos = sorted(np.random.randint(0,N,2))
            while (pos[0] == (N-1)): # Evitar que ambos sean iguales a N-1
                pos = sorted(np.random.randint(0,N,2))
            hijos[pos[0],i], hijos[pos[1],i] = hijos[pos[1],i], hijos[pos[0],i]

            
    return(hijos)

def mutacionInver(hijos,pm,N):
    """
    Mutación por inversión.

    Args:
        hijos (matrix): Matriz con los hijos a mutar.
        pm (float): Probabilidad de mutación.
        N 
    
    Returns:
        int matrix: Matriz con los hijos mutados.
    """
   # invertir los elementos de la subcadena contenida entre ellos
    for i in range(2):
      a = np.random.uniform()
      if(a < pm):
         pos = sorted(random.sample(range(N),2)) # Tomo dos índices cualquiera, ordenados de menor a mayor
         hijos[pos[0]:pos[1]+1, i] = np.flip(hijos[pos[0]:pos[1]+1, i])

    return(hijos)

def supervivientesElite(poblacion,fitness,matrizHijos,fitnessHijos,popSize,N,numPadres, Ntop):
    """
    Selección de supervivientes elitista.

    Args:
        poblacion (int matrix): Matriz con la población de cromosomas
        fitness (float array): Array con los valores de fitness de la población
        matrizHijos (int matrix): Matriz con los hijos
        fitnessHijos (float array): Array con los valores de fitness de los hijos
        popSize (int): Tamaño de la población de cromosomas
        N (int): Tamaño de la permutación
        numPadres (int): Número de padres
        Ntop (int): Número de padres que se seleccionan de manera elitista

    Returns:
        int matrix: Matriz con los supervivientes seleccionados.
    """    
    generacionActual = np.zeros([popSize+numPadres,N])
    generacionActual[0:popSize,:] = poblacion
    generacionActual[(popSize):(popSize+numPadres),:] = matrizHijos

    fitnessGeneracion = np.zeros(popSize+numPadres)

    fitnessGeneracion[0:popSize] = fitness
    fitnessGeneracion[popSize:popSize+numPadres] = fitnessHijos
    
    orden = np.argsort(fitnessGeneracion) 
    
    supervivientes = np.zeros([popSize,N+1])
    supervivientes[:,0:N]=generacionActual[orden[0:popSize],:]
    supervivientes[:,N]=fitnessGeneracion[orden[0:popSize]]
    
    return(supervivientes)

def supervivientesMix(poblacion,fitness,matrizHijos,fitnessHijos,popSize,N,numPadres, Ntop):
    """
    Selección de supervivientes mix: elitista + random.

    Args:
        poblacion (int matrix): Matriz con la población de cromosomas
        fitness (float array): Array con los valores de fitness de la población
        matrizHijos (int matrix): Matriz con los hijos
        fitnessHijos (float array): Array con los valores de fitness de los hijos
        popSize (int): Tamaño de la población de cromosomas
        N (int): Tamaño de la permutación
        numPadres (int): Número de padres
        Ntop (int): Número de padres que se seleccionan de manera elitista

    Returns:
        int matrix: Matriz con los supervivientes seleccionados.
    """    
    
    # Selección elitista + no tan buenos
    generacionActual = np.zeros([popSize+numPadres,N])
    generacionActual[0:popSize,:] = poblacion
    generacionActual[(popSize):(popSize+numPadres),:] = matrizHijos

    fitnessGeneracion = np.zeros(popSize+numPadres)

    fitnessGeneracion[0:popSize] = fitness
    fitnessGeneracion[popSize:popSize+numPadres] = fitnessHijos
    
    orden = np.argsort(fitnessGeneracion) 
    indices_elite = orden[0:Ntop]
    indices_NoElite = random.sample(list(orden[Ntop:]), popSize-Ntop)
    
    supervivientes = np.zeros([popSize,N+1])
    supervivientes[0:Ntop, 0:N]=generacionActual[indices_elite,:]
    supervivientes[Ntop:popSize, 0:N]=generacionActual[indices_NoElite,:]
    supervivientes[:,N]=fitnessGeneracion[np.concatenate((indices_elite, indices_NoElite))]
    
    return supervivientes

def genetico_QAP(popSize,numPadres,pm,numIteraciones,ficheroDistancias, ficheroFlujos, 
                 flagSpadres, flagSupervivientes, flagMutacion, flagCruce,
                 rtop = 0.3):
    """
    Algoritmo genético para tratar el QAP.

    Args:
        popSize (int): Tamaño de la población de cromosomas
        numPadres (int): Número de padres 
        pm (float): Probabilidad de mutación
        numIteraciones (int): Número de iteraciones del algoritmo hasta la parada
        ficheroDistancias (string): Ruta al archivo .txt con la matriz de distancias
        ficheroFlujos (string): Ruta al archivo .txt con la matriz de flujos
        flagSpadres (int): Valor 0 o 1 para decidir cómo se hace la selección de padres
        flagSupervivientes (int): Valor 0 o 1 para decidir cómo se hace la elección de supervivientes
        flagMutacion (int): Valor 0 o 1 para decidir cómo se hace la mutación
        flagCruce (int): Valor 0 o 1 para decidir cómo se hace el cruce
        rtop (float): Coeficiente entre 0 y 1 de padres elegidos de manera elitista en la selección
        de supervivientes mix. Valor por defecto es 0.3

    Returns:
        float array: Array de tamaño numIteraciones con el valor mínimo de fitness alcanzado en cada
        iteración.
    """    
    
    distancias = np.loadtxt(ficheroDistancias)
    flujos = np.loadtxt(ficheroFlujos)
    N = flujos.shape[0]
    Ntop = int(rtop*popSize)
    minimos = []
    
    
    if (numPadres%2==1): # Para que el número de padres sea par, nos aseguramos
        numPadres = numPadres-1

    # Poblacion inicial
    poblacion = np.zeros([popSize,N])
    fitness = np.zeros(popSize) # Valores de funcion objetivo de cada elemento de la poblacion
    
    for i in range(popSize):
        poblacion[i,] = np.random.permutation(N)
        fitness[i] = evaluaFO(poblacion[i,], flujos, distancias)
  
    # Bucle principal. Criterio de parada: número de iteraciones
    for jj in range(numIteraciones):
        matrizHijos = np.zeros([numPadres,N])
        for kk in range(int(numPadres/2)): # Eligo 2 padres un numero de veces igual a numPadres/2 (de ahi que quisiéramos que fuese par)
            
            
            # Posibles métodos de selección de padres
            if(flagSpadres == 0): 
                # Seleccion de padres al azar
                quienes = random.sample(range(popSize),2)
                while(quienes[0] == quienes[1]): # Padres distintos
                    quienes = random.sample(range(popSize),2)
                candidato1 = quienes[0]
                candidato2 = quienes[1]
            else:
                # Seleccion de padres por torneo (cojo 2 y me quedo con el mejor, dos veces)
                quienes = random.sample(range(popSize),2)
                v = np.argsort(fitness[quienes]) # Me ordena de menor a mayor y me devuelve los índices
                u = v[0] # Me interesa el menor, o sea, el primero
                candidato1 = quienes[u] 
                
                quienes = random.sample(range(popSize),2)
                v = np.argsort(fitness[quienes]) # Me ordena de menor a mayor y me devuelve los índices
                u = v[0] # Me interesa el menor, o sea, el último
                candidato2 = quienes[u]
            
            
            # Crossover de los 2 progenitores elegidos
            if (flagCruce == 0):
                hijos = cruceO(poblacion[candidato1,],poblacion[candidato2,],N)
            else:
                hijos = crucePM(poblacion[candidato1,],poblacion[candidato2,],N)
    
            # Mutación
            if (flagMutacion == 0):
                hijos = mutacionInver(hijos,pm,N)
                hijos = np.transpose(hijos)
            else:
                hijos = mutacionInter(hijos, pm, N)
                hijos = np.transpose(hijos)

            # Guardo los hijos
            matrizHijos[(kk*2):(kk*2+2),:] = hijos
        
        # Evaluación de hijos
        fitnessHijos = np.zeros(numPadres)
    
        for i in range(numPadres):
            fitnessHijos[i] = evaluaFO(matrizHijos[i,], flujos, distancias)
     
        # Selección supervivientes
        if (flagSupervivientes == 0):
            res = supervivientesMix(poblacion,fitness,matrizHijos,fitnessHijos,popSize,N,numPadres, Ntop)
        else:
            res = supervivientesElite(poblacion,fitness,matrizHijos,fitnessHijos,popSize,N,numPadres, Ntop)
        
        
        poblacion = res[:,0:N]
        fitness = res[:,N]
        
        minimos.append(min(fitness)) # Guardo el mínimo de la iteración
        
    
    # Devolvemos el resultado final
    return minimos

