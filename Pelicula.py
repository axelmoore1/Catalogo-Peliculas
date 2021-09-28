class Pelicula:
    def __init__(self, nombre):
        self._nombre = nombre


    def __str__(self):
        return f'Pelicula: {self._nombre}'


    def getNombre(self):
        return self._nombre


    def setNombre(self, nombre):
        self._nombre = nombre