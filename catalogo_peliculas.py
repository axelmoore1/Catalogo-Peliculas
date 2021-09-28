import os


class CatalogoPeliculas:


    ruta_archivo = 'peliculas.txt'


    @classmethod
    def agregarPelicula(cls, pelicula):
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula._nombre}\n')

    @classmethod
    def listarPeliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
            print('Catalogo de peliculas'.center(50, '-'))
            print(archivo.read())


    @classmethod
    def eliminarPeliculas(cls):
        os.remove(cls.ruta_archivo)
        print('Archivo eliminado: ', cls.ruta_archivo)