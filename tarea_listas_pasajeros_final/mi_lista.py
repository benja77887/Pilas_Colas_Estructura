class MiLista:
    """Lista construida manualmente sobre un arreglo de tamaño fijo."""

    def __init__(self, capacidad=10):
        if capacidad < 0:
            raise ValueError("La capacidad no puede ser negativa")
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def añadir(self, pasajero):
        # No se permiten números de pasajero repetidos.
        if self.buscar(pasajero.numero) != -1:
            print("  ⚠ Ya existe un pasajero con ese número")
            return False
        if self.cantidad == self.capacidad:
            print("  ⚠ La lista está llena")
            return False
        self.datos[self.cantidad] = pasajero
        self.cantidad += 1
        return True

    def listar(self):
        if self.cantidad == 0:
            print("  (lista vacía)")
            return
        for i in range(self.cantidad):
            print(f"  [{i}] {self.datos[i]}")

    def insertar(self, posicion, pasajero):
        # La posición final también es válida: 0 <= posicion <= cantidad.
        if posicion < 0 or posicion > self.cantidad:
            print("  ⚠ Posición fuera de rango")
            return False
        if self.cantidad == self.capacidad:
            print("  ⚠ La lista está llena")
            return False
        if self.buscar(pasajero.numero) != -1:
            print("  ⚠ Ya existe un pasajero con ese número")
            return False

        # Desplaza de atrás hacia adelante para dejar libre la posición.
        i = self.cantidad
        while i > posicion:
            self.datos[i] = self.datos[i - 1]
            i -= 1
        self.datos[posicion] = pasajero
        self.cantidad += 1
        return True

    def buscar(self, numero):
        # Búsqueda lineal: revisa desde la posición 0 hasta cantidad - 1.
        for i in range(self.cantidad):
            if self.datos[i].numero == numero:
                return i
        return -1

    def buscar_binaria(self, numero):
        # Requiere que los pasajeros estén ordenados por número ascendente.
        izq = 0
        der = self.cantidad - 1
        while izq <= der:
            medio = (izq + der) // 2
            actual = self.datos[medio].numero
            if actual == numero:
                return medio
            if actual < numero:
                izq = medio + 1
            else:
                der = medio - 1
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        posicion = self.buscar(numero)
        if posicion == -1:
            return False
        self.datos[posicion].destino = nuevo_destino
        self.datos[posicion].asiento = nuevo_asiento
        return True

    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= self.cantidad:
            print("  ⚠ Posición fuera de rango")
            return None

        pasajero = self.datos[posicion]
        # Desplaza hacia la izquierda y limpia el último cajón ocupado.
        i = posicion
        while i < self.cantidad - 1:
            self.datos[i] = self.datos[i + 1]
            i += 1
        self.cantidad -= 1
        self.datos[self.cantidad] = None
        return pasajero

    def eliminar_por_valor(self, numero):
        # Reutiliza buscar y eliminar_por_posicion; no repite el recorrido.
        posicion = self.buscar(numero)
        if posicion == -1:
            return False
        self.eliminar_por_posicion(posicion)
        return True

    def ordenar_asc(self):
        # Burbuja: un pasajero se compara con el que está a su derecha.
        for i in range(self.cantidad - 1):
            for j in range(self.cantidad - 1 - i):
                if self.datos[j].numero > self.datos[j + 1].numero:
                    aux = self.datos[j]
                    self.datos[j] = self.datos[j + 1]
                    self.datos[j + 1] = aux

    def ordenar_desc(self):
        # Es la misma burbuja; solo cambia > por <.
        for i in range(self.cantidad - 1):
            for j in range(self.cantidad - 1 - i):
                if self.datos[j].numero < self.datos[j + 1].numero:
                    aux = self.datos[j]
                    self.datos[j] = self.datos[j + 1]
                    self.datos[j + 1] = aux

    def reversar(self):
        izq = 0
        der = self.cantidad - 1
        while izq < der:
            aux = self.datos[izq]
            self.datos[izq] = self.datos[der]
            self.datos[der] = aux
            izq += 1
            der -= 1

    def copiar(self):
        nueva = MiLista(self.capacidad)
        for i in range(self.cantidad):
            nueva.añadir(self.datos[i])
        return nueva

    def longitud(self):
        return self.cantidad
