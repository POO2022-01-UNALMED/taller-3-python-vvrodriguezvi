class Marca:

    #Constructor

    def __init__(self, nombre):
        self._nombre = nombre

    #Get y Set de nombre
    
    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre
