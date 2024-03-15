"""
Palabras de markov
"""
import random
import re

"""Palabras de Markov"""

"""Viene de https://www.youtube.com/watch?v=8ext9G7xspg&t=9109s
    - Leer un texto
    - Crear un grafo donde:
        - cada nodo son palabras
        - cada palabra tiene una lista de palabras siguientes
        con la frecuencia en que son 'siguientes' según el texto
    - Luego se selecciona una palabra y se navega el grafo
    aleatoriamente según el peso de cada palabra siguiente.
"""

INICIO_FRASE = "_INICIO_FRASE_"
FINAL_FRASE = "_FINAL_FRASE_"


def crear_texto(fichero):
    """Crear 'texto' a partir de un fichero"""
    with open(fichero, encoding="utf-8") as f:
        read_data = f.read()
    return read_data


def crear_dict_palabras(texto):
    """Leer texto"""

    def agrega_a_palabra_anterior(pal, anterior):
        """Exactamente eso"""
        if pal not in palabras[anterior]:
            palabras[anterior][pal] = 0
        palabras[anterior][pal] += 1

    def separar_palabras_str(anterior):
        """Separar palabras usando métodos de string"""
        # Las palabras compuestas separadas por "-" quedan unidas...
        # Quitar los separadores: , . : ; ...
        # separadores = ".:,;¡¿!?()[]{}ªº0123456789-_"
        sep_sin_punto = ":,;¡¿!?()[]{}ªº0123456789-_"

        for pal in texto.split():
            if not pal.isalpha():
                for char in sep_sin_punto:
                    nueva_pal = pal.replace(char, "")
                    pal = nueva_pal
                    if pal.isalpha() or pal == "" or pal.strip(".").isalpha():
                        break
            if pal == "":
                continue

            if pal not in palabras:
                palabras[pal] = {}

            # if anterior == "":
            #     anterior = pal
            #     continue

            agrega_a_palabra_anterior(pal, anterior)

            # Si es final de frase...
            if not pal.isalpha() and pal.strip(".").isalpha():
                anterior = pal
                pal = FINAL_FRASE
                agrega_a_palabra_anterior(pal, anterior)
                anterior = INICIO_FRASE
            else:
                anterior = pal

    def separar_palabras_re(anterior):
        """Separar palabras usando métodos de re"""
        # patron_split = re.compile(r'\W')
        patron_split = re.compile(r'[^\w.]')
        pal_sin_punto = re.compile(r'.*[^.]$')

        for pal in patron_split.split(texto):
            if pal not in palabras:
                palabras[pal] = {}

            agrega_a_palabra_anterior(pal, anterior)

            # Si es final de frase - tiene punto...
            obj_2 = pal_sin_punto.search(pal)
            if obj_2 is None:
                anterior = pal
                pal = FINAL_FRASE
                agrega_a_palabra_anterior(pal, anterior)
                anterior = INICIO_FRASE
            else:
                anterior = pal

    palabras = {}
    palabras[INICIO_FRASE] = {}
    palabras[FINAL_FRASE] = {}
    anterior = INICIO_FRASE

    # separar_palabras_str(anterior)
    separar_palabras_re(anterior)
    return palabras


def elegir_palabra(palabras):
    """Elegir una palabra para el inicio del grafo"""
    while True:
        print("Palabras disponibles")
        for pal in palabras:
            print(pal, end=" ")
        print()
        pal = input("Escriba la palabra por la que comenzar: ")
        if pal in palabras:
            return pal


# def elegir_inicio(palabras):
#     pass


# def escibir_grafo(inicio):
def escibir_grafo(palabras):
    """Esribir grafo a partir de palabra de inicio"""
    # print(inicio, end=" ")
    # pal = inicio
    for _ in range(3):
        pal = INICIO_FRASE
        while True:
            peso_total = 0
            pal_sig = {}
            for siguiente, peso in palabras[pal].items():
                peso_total += peso
                pal_sig[peso_total] = siguiente
            if peso_total == 0 or siguiente == FINAL_FRASE:
                break

            peso_sig = random.randint(1, peso_total)
            for peso_pal in sorted(pal_sig.keys()):
                if peso_sig <= peso_pal:
                    pal = pal_sig[peso_pal]
                    print(pal_sig[peso_pal], end=" ")
                    break

        print()


def programa_principal():
    """Programa principal"""
    texto = "I am, subscribed to Y-Cubed and I am 123 loving678 it."
    texto = "I am, subscribed to Y Cubed. and I am 123 loving678 it."

    fichero = "el_quijote.txt"
    # fichero = "prueba.txt"
    texto = crear_texto(fichero)
    palabras = crear_dict_palabras(texto)
    # print(palabras[FINAL_FRASE])
    # inicio = elegir_palabra(palabras)
    # escibir_grafo(INICIO_FRASE)
    escibir_grafo(palabras)


if __name__ == "__main__":
    programa_principal()
