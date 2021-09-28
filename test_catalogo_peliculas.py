from Dominio.Pelicula import Pelicula
from Servicios.catalogo_peliculas import CatalogoPeliculas
opcion = None
while opcion != 4:
    try:
        print('Opciones:')
        print('1. Agregar Peliculas')
        print('2. Listar Peliculas')
        print('3. Eliminar catalogo de peliculas')
        print('4. Salir')
        opcion = int(input("Ingrese opcion (1-4) "))

        if opcion == 1:
            nombre_pelicula = input("Ingrese nombre de pelicula: ")
            pelicula = Pelicula(nombre_pelicula)
            CatalogoPeliculas.agregarPelicula(nombre_pelicula)
        elif opcion == 2:
            CatalogoPeliculas.listarPeliculas()
        elif opcion == 3:
            CatalogoPeliculas.eliminarPeliculas()

    except Exception as e:
        print(f'Ocurrio un error {e}')
        opcion = None
else:
    print('Salimos del programa')