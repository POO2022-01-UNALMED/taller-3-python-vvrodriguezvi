class TV:

    numTV = 0 #iniciar el contador del # de tvs

    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        self._control = None
        self.__class__.numTV += 1

    
    # Getter ans setters

    def getMarca(self):
        return self._marca

    def getControl(self):
        return self._control

    def getPrecio(self):
        return self._precio

    def getVolumen(self):
        return self._volumen

    def getCanal(self):
        return self._canal

    def setMarca(self, marca):
        self._marca = marca

    def setControl(self,control):
        self._control = control

    def setPrecio(self, precio):
        self._precio = precio

    
    def setVolumen(self, volumen):
        if (volumen>= 0 and volumen<=7 and self._estado):
            self._volumen = volumen

    def setCanal(self, canal):
        if (canal>0 and canal<=120 and self._estado):
            self._canal = canal
    
    def getEstado(self):
        return self._estado

    def setEstado(self, estado):
        self._estado = estado

    # Metodos de clase

    @classmethod
    def setNumTV(cls, numTV):
        cls.numTV = numTV
    
    @classmethod
    def getNumTV(cls):
        return cls.numTV

    # METODOS DE INSTANCIA

    # encendido o no

    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = True

    #Canal (control)

    def canalUp(self):
        if (self._estado):
            if (self._canal != 120):
                self._canal += 1
            else:
                self._canal = 1

    def canalDown(self):
        if (self._estado):
            if (self._canal != 1):
                self._canal -= 1
            else:
                self._canal = 120

    #Volumen (control)
    def volumenUp(self):
        if (self._estado):
            if (self._volumen < 7):
                self._volumen += 1

    def volumenDown(self):
        if (self._estado):
            if (self._volumen > 0):
                self._volumen -= 1

