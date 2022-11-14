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

val = [21, 11, 15, 9, 34, 25, 41, 52, 30, 58]
wt = [22, 12, 16, 10, 35, 26, 42, 53, 39, 5]

W = 100

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

    with open("basic.csv", "a") as archivo:
        archivo.write(formato_datos.format(time_python, time_cython))

    print("Cython Time: ",time_cython)
    print("Python Time: ",time_python)

    print("Cython es: ",time_python/time_cython," más rapido")
    print()
    