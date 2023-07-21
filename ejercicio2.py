from math import pi

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return pi * self.radio ** 2
    def perimetro(self):
        return 2 * pi * self.radio
    
circulo1 = Circulo(5)
print (f'El area del circulo es {circulo1.area()}')
print (f'El perimetro del circulo es {circulo1.area()}')

circulo2 = Circulo(10)
print (f'El area del circulo es {circulo2.area()}')
print (f'El perimetro del circulo es {circulo2.area()}')
        
        