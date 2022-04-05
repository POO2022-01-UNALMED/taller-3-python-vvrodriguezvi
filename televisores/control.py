class Control:

    #Constructor
 
    def __ini__(self, tv):
        self._tv = None

    # Enlazar

    def enlazar(self, tv):
        self._tv = tv
        self._tv.setControl(self) 

    #Getter and setter

    def gettv(self):
        return self._tv

    def settv(self, tv):
        self._tv = tv
    
    def setCanal(self, canal):
        self._tv.setCanal(canal)

    #metodos

    # Subir o bajar volumen
    
    def volumenUp(self):
        self._tv.volumenUp()
        
    def volumenDown(self):
        self._tv.volumenDown()

    
    #Prender y apagar

    def turnOn(self):
        self._tv.turnOn()

    
    def turnOff(self):
        self._tv.turnOff()

    #Subir o bajar canal

    def canalUp(self):
        self._tv.canalUp()
    
    def canalDown(self):
        self._tv.canalDown()
