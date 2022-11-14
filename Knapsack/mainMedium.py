"""
- Fecha: 20 nov 2022
- Autor: Paula Godoy / Sofía Orjuela 
- Tema: Cython
- Tópico: Knapsack Problem
- Principal: Llama a ambos programas (Cy/Py)
"""

import knapsack_cy
import knapsack_py
import time

val = [360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147, 78, 256, 63, 17, 
       120, 164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28, 87, 73, 78, 15, 26, 78, 210, 36, 
       85, 189, 274, 43, 33, 10, 19, 389, 276, 312]

wt = [7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 0,
        42, 47, 52, 32, 26, 48, 55, 6, 29, 84, 2, 4, 18, 56, 7, 29, 93, 44, 71, 3,
         86, 66, 31, 65, 0, 79, 20, 65, 52, 13]
         
W = 850

# Se crea un formato para la impreión sobre el fichero
formato_datos = "{:.7f}, {:7f}\n"

for i in range(10):
    
    # Toma de tiempos para Python
    ini_time = time.time()
    knapsack_py.knapSack(W, wt, val)
    fin_time = time.time()

    time_python = fin_time-ini_time

    # Toma de tiempos para Cython
    ini_time = time.time()
    knapsack_cy.knapSack(W, wt, val)
    fin_time = time.time()

    time_cython = fin_time-ini_time

    with open("medium.csv", "a") as archivo:
        archivo.write(formato_datos.format(time_python, time_cython))

    print("Cython Time: ",time_cython)
    print("Python Time: ",time_python)

    print("Cython es: ",time_python/time_cython," más rapido")
    print()
    