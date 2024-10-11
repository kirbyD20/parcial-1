def is_subsequence(lst, seq):
    """
    Verificar si el array_list seq es una sub-secuencia del array_list lst.

    :param lst: array_list de enteros.
    :type lst: dict (representando una lista array_list)
    :param seq: array_list de enteros a verificar si es sub-secuencia de lst.
    :type seq: dict (representando una lista array_list)

    return True si seq es una sub-secuencia de lst, False de lo contrario.
    """
    respuesta = False
    for i in range(lst['size']):
        pos_lst= lst['pos'][i]
        for j in range(seq['size']):
            pos_seq= lst['pos'][j]
            if lst[i] >= seq[j] and seq[j] in lst[i] :
                respuesta = True
    return respuesta

class Cine:
    def __init__(self, filas, columnas):
        # Inicializa la sala del cine con sillas vacías (False)
        self.salas = [[False for _ in range(columnas)] for _ in range(filas)]

    def ocupar_silla(self, fila, columna):
        # Marca una silla como ocupada
        if self.salas[fila][columna] is False:
            self.salas[fila][columna] = True
            print(f"Silla en fila {fila + 1}, columna {columna + 1} ocupada.")
        else:
            print(f"La silla en fila {fila + 1}, columna {columna + 1} ya está ocupada.")

    def mostrar_sillas_vacias(self):
        print("Sillas vacías en el cine:")
        for fila in range(len(self.salas)):
            for columna in range(len(self.salas[fila])):
                if not self.salas[fila][columna]:
                    print(f"Silla en fila {fila + 1}, columna {columna + 1} está vacía.")

# Ejemplo de uso
if __name__ == "__main__":
    cine = Cine(filas=5, columnas=5)  # Crea un cine de 5x5

    # Ocupar algunas sillas
    cine.ocupar_silla(0, 1)  # Ocupa la silla (1, 2)
    cine.ocupar_silla(2, 3)  # Ocupa la silla (3, 4)
    cine.ocupar_silla(4, 0)  # Ocupa la silla (5, 1)

    # Mostrar las sillas vacías
    cine.mostrar_sillas_vacias()

def factorial(n):
    # Caso base: el factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    else:
        # Llamada recursiva
        return n * factorial(n - 1)

# Ejemplo de uso
if __name__ == "__main__":
    numero = 5
    resultado = factorial(numero)
    print(f"El factorial de {numero} es: {resultado}")
