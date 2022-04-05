class TV:

    cont = 0 #iniciar el contador del # de tvs

    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        TV.cont += 1

    
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
        if (volumen>= 0 and volumen<=7 and self._estado == True):
            self._volumen = volumen

    def setCanal(self, canal):
        if (canal>0 and canal<=120 and self._estado == True):
            self._canal = canal


    # Metodos
    
    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = True

    def getEstado(self):
        return self._estado

    def setEstado(self, estado):
        self._estado = estado

    def canalUp(self):
        self.setCanal(self._canal+1)

    def canalDown(self):
        self.setCanal(self._canal-1)

    def volumenUp(self):
        self.setVolumen(self._volumen+1)

    def volumenDown(self):
        self.setVolumen(self._volumen-1) 
