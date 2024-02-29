Viene de https://www.youtube.com/watch?v=8ext9G7xspg&t=9109s
    - Leer un texto
    - Crear un grafo donde:
        - cada nodo son palabras
        - cada palabra tiene una lista de palabras siguientes
        con la frecuencia en que son 'siguientes' según el texto
    - Luego se selecciona una palabra y se navega el grafo
    aleatoriamente según el peso de cada palabra siguiente.

La idea es poder leer textos como "El Quijote" para luego crear otros textos.

Falta marcar los inicios y finales de oraciones y elegir cuantas frases crear.

También falta ordenar mejor el código actual.

2024-02-29: 
Refactoring inicial hecho.

Mejoras propuestas:
- Leer frases desde un fichero. -->2024-02-29 ¡Hecho!
- Agregar inicios de frase en lista de palabras para elegir el inicio aleatoriamente. -->2024-02-29 ¡Hecho!
- Dejar los puntos al final de la frase para marcar finales de frase. -->2024-02-29 ¡Hecho!
- Estudiar si dejamos ',' ':', y otros signos de puntuación.
- Agregar cuántas frases queremos sacar.
- Leer desde fichero .env el texto a leer y/o los separadores a omitir.
