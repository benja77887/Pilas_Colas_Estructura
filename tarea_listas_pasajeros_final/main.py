from pasajero import Pasajero
from mi_lista import MiLista
from lista_python import ListaPython

lista1 = MiLista(10)
lista2 = ListaPython()


def leer_entero(mensaje):
    """Repite la pregunta hasta que se ingrese un entero válido."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ingresar un número entero.")


def leer_texto(mensaje):
    """Evita aceptar campos de texto vacíos."""
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("  Este campo no puede quedar vacío.")


def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    while numero <= 0:
        print("  El número de pasajero debe ser positivo.")
        numero = leer_entero("  N.º de pasajero: ")

    nombre = leer_texto("  Nombre: ")
    cedula = leer_texto("  Cédula: ")
    edad = leer_entero("  Edad: ")
    while edad < 0:
        print("  La edad no puede ser negativa.")
        edad = leer_entero("  Edad: ")
    fecha = leer_texto("  Fecha de vuelo (AAAA-MM-DD): ")
    destino = leer_texto("  Destino: ")
    asiento = leer_texto("  Asiento: ").upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def cargar_datos_prueba(lista):
    datos = [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito", "12A"),
        Pasajero(1002, "Ana", "0912345678", 28, "2026-11-15", "Lima", "03C"),
        Pasajero(1009, "Luis", "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto", "0934567890", 16, "2026-11-20", "Quito", "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima", "01A"),
    ]
    añadidos = 0
    for pasajero in datos:
        if lista.añadir(pasajero):
            añadidos += 1
    print(f"  ✓ Datos de prueba procesados; nuevos pasajeros: {añadidos}")


def mostrar_opciones(titulo, extras=False):
    print(f"\n========== {titulo} ==========")
    print(" 1. Añadir           2. Listar            3. Insertar en posición")
    print(" 4. Buscar (lineal)  5. Buscar (binaria)  6. Modificar")
    print(" 7. Eliminar por posición                 8. Eliminar por número")
    print(" 9. Ordenar asc     10. Ordenar desc     11. Reversar")
    print("12. Copiar          13. Longitud")
    if extras:
        print("14. Filtrar por destino                  15. Mayores de edad")
    print(" C. Cargar datos de prueba                0. Volver")
    print(" Nota: la búsqueda binaria requiere ordenar ascendentemente primero.")


def pasajeros_de(lista):
    """Devuelve el arreglo ocupado de MiLista o la lista de ListaPython."""
    if isinstance(lista, MiLista):
        return lista.datos
    return lista.pasajeros


def ejecutar_menu(lista, extras=False):
    titulo = "MENÚ 2 · list de Python" if extras else "MENÚ 1 · MiLista"
    while True:
        mostrar_opciones(titulo, extras)
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if lista.añadir(pasajero):
                print("  ✓ Pasajero añadido")
        elif op == "2":
            lista.listar()
        elif op == "3":
            posicion = leer_entero("  Posición donde insertar: ")
            pasajero = leer_pasajero()
            if lista.insertar(posicion, pasajero):
                print("  ✓ Pasajero insertado")
        elif op == "4":
            numero = leer_entero("  Número de pasajero a buscar: ")
            posicion = lista.buscar(numero)
            if posicion == -1:
                print("  No existe ese pasajero")
            else:
                print(f"  Encontrado en [{posicion}]: {pasajeros_de(lista)[posicion].nombre}")
        elif op == "5":
            numero = leer_entero("  Número a buscar: ")
            posicion = lista.buscar_binaria(numero)
            if posicion == -1:
                print("  No se encontró. Compruebe que la lista esté ordenada ascendentemente.")
            else:
                print(f"  Encontrado en [{posicion}]: {pasajeros_de(lista)[posicion].nombre}")
        elif op == "6":
            numero = leer_entero("  Número de pasajero a modificar: ")
            destino = leer_texto("  Nuevo destino: ")
            asiento = leer_texto("  Nuevo asiento: ").upper()
            if lista.modificar(numero, destino, asiento):
                print("  ✓ Pasajero modificado")
            else:
                print("  No existe ese pasajero")
        elif op == "7":
            posicion = leer_entero("  Posición que desea eliminar: ")
            pasajero = lista.eliminar_por_posicion(posicion)
            if pasajero is not None:
                print(f"  ✓ Eliminado: {pasajero.nombre}")
        elif op == "8":
            numero = leer_entero("  Número de pasajero que desea eliminar: ")
            if lista.eliminar_por_valor(numero):
                print("  ✓ Pasajero eliminado")
            else:
                print("  No existe ese pasajero")
        elif op == "9":
            lista.ordenar_asc()
            print("  ✓ Lista ordenada de menor a mayor")
        elif op == "10":
            lista.ordenar_desc()
            print("  ✓ Lista ordenada de mayor a menor")
        elif op == "11":
            lista.reversar()
            print("  ✓ Lista reversada")
        elif op == "12":
            copia = lista.copiar()
            copia.reversar()
            print("  ✓ Copia creada y reversada (el original no cambia)")
            copia.listar()
        elif op == "13":
            print(f"  Cantidad de pasajeros: {lista.longitud()}")
        elif op == "14" and extras:
            destino = leer_texto("  Destino que desea filtrar: ")
            filtrados = lista.filtrar_por_destino(destino)
            if filtrados:
                for i, pasajero in enumerate(filtrados):
                    print(f"  [{i}] {pasajero}")
            else:
                print("  No hay pasajeros para ese destino")
        elif op == "15" and extras:
            mayores = lista.mayores_de_edad()
            if mayores:
                for i, pasajero in enumerate(mayores):
                    print(f"  [{i}] {pasajero}")
            else:
                print("  No hay pasajeros mayores de edad")
        elif op == "C":
            cargar_datos_prueba(lista)
        elif op == "0":
            break
        else:
            print("  Opción no válida")


def menu_lista1():
    ejecutar_menu(lista1)


def menu_lista2():
    ejecutar_menu(lista2, extras=True)


def main():
    while True:
        print("\n===== TAREA LISTAS · PASAJEROS ✈ =====")
        print("1. Menú 1 · MiLista")
        print("2. Menú 2 · list de Python")
        print("3. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            menu_lista1()
        elif op == "2":
            menu_lista2()
        elif op == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
