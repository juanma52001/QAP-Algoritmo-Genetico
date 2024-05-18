class GeneralConfig:
    """
    Clase que contiene los parametros generales de la ejecucion del algoritmo genetico
    """    
    def __init__(self, Spadres, Super, Mutacion, Cruce, MatrizD, MatrizF, NumPob, NumPadres, pm, ratio, avg_min = None, avg_Niter = None):
        """
        Constructor de la clase GeneralConfig

        Args:
            Spadres (int): Entero que descibe el tipo de seleccion de padres.
            Super (int): Entero que descibe el tipo de seleccion de supervivientes.
            Mutacion (int): Entero que descibe el tipo de mutacion.
            Cruce (int): Entero que descibe el tipo de cruce.
            MatrizD (string): Archivo de texto que contiene la matriz de distancias.
            MatrizF (string): Archivo de texto que contiene la matriz de flujos.
            NumPob (int): Entero que descibe el numero de individuos en la poblacion.
            NumPadres (int): Entero que descibe el numero de padres que se seleccionan.
            pm (float): Probabilidad de mutacion.
            ratio (float, optional): Proporción de padres elegidos de manera elitista en una selección mixta.
            avg_min (float list, optional): Lista que guarda el fitness mínimo medio en cada iteración del algorimo genético. None por defecto.
            avg_Niter (float list, optional): Lista que guarda la iteración de convergencia media en cada repetición del algoritmo genético. None por defecto.
        """
        self.Spadres = Spadres
        self.Supervivientes = Super
        self.Mutacion = Mutacion
        self.Cruce = Cruce
        self.MatrizD = MatrizD
        self.MatrizF = MatrizF
        self.NumPob = NumPob
        self.NumPadres = NumPadres
        self.pm = pm
        self.ratio = ratio
        self.avg_min = avg_min 
        self.avg_Niter = avg_Niter 