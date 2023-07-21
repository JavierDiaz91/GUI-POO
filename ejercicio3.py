class Estudiante:
    def __init__(self, nombre, edad, notas):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas

    def promedio(self):
        return sum(self.notas) /len(self.notas)
    
    def esAprobado(self):
        prom = self.promedio()
        return prom >= 60
    
estudiante1 = Estudiante("Juan", 20, [8, 6, 9, 4])
estudiante1.promedio()

if estudiante1.esAprobado:
    print(f"El estudiante {estudiante1.nombre} aprobado")
else:
    print(f"El estudiante {estudiante1.nombre} desaprobo")