class Libro:
    def __init__(self, titulo, autor, añoPublicacion): 
        self.titulo = titulo
        self.autor = autor
        self.añoPublicacion = añoPublicacion

    def mostrarInformacion(self):
        print(f"El titulo del libro es:  {self.titulo}")
        print(f"El nombre del autor es:  {self.autor}")
        print(f"El año de publicacion del libro fue:  {self.añoPublicacion}")

    def esAntiguo(self):
        return self.año < 2000
    
libro1 = Libro("Antartida", "Euler", 1978)

libro1.mostrarInformacion()

if libro1.esAntiguo:
    print("El libro es antiguo")
else:
    print("El libro es nuevo")

    