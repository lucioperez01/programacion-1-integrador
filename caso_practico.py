import matplotlib.pyplot as plt
import random
import timeit


#algoritmos de ordenamiento ↓
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def insertion_sort(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Encontrar el índice del elemento mínimo
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Intercambiar el elemento mínimo con el elemento actual
        arr[i], arr[min_index] = arr[min_index], arr[i]

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

#medicion de tiempos
def medidor_de_tiempos(funcion, lista):
    lista_copia = lista.copy()
    tiempo_inicial = timeit.default_timer()
    resultado = funcion(lista_copia)
    tiempo_final = timeit.default_timer()
    return tiempo_final - tiempo_inicial

def graficar():
    #grafica las líneas del grafico↓
    plt.plot(tamaños, tiempos_eleccion1, label=f"{eleccion1}", color="red", marker="o")
    plt.plot(tamaños, tiempos_eleccion2, label=f"{eleccion2}", color="blue", marker="s")
# Etiquetas
    plt.title("Comparación de Algoritmos de Ordenamiento")
    plt.xlabel("Cantidad de elementos")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)
    #plt.tight_layout()
    plt.show()

#Creacion de listas con 100, 500, 1.000, 5.000 y 10.000 elementos
lista100 = [random.randint(1,10000) for i in range(100)]
lista500 = [random.randint(1,10000) for i in range(500)]
lista1000 = [random.randint(1,10000) for i in range(1000)]
lista5000 = [random.randint(1,10000) for i in range(5000)]
lista10000 = [random.randint(1,10000) for i in range(10000)]


#interfaz de usuario
eleccion1 = int(input("Ingrese el algoritmo que desea comparar: \n1: Bubble Sort \n2: Insertion Sort \n3: Selection Sort \n4: Quicksort \n5: Sorted()): \n"))
eleccion2 = int(input("Ingrese el segundo algoritmo que desea comparar: \n1: Bubble Sort \n2: Insertion Sort \n3: Selection Sort \n4: Quicksort \n5: Sorted()): \n"))

if eleccion1 == 1:
    eleccion1 = "Bubble Sort"
    funcion1 = bubble_sort
elif eleccion1 == 2:
    eleccion1 = "Insertion Sort"
    funcion1 = insertion_sort
elif eleccion1 == 3:
    eleccion1 = "Selection Sort"
    funcion1 = selection_sort
elif eleccion1 == 4:
    eleccion1 = "Quicksort"
    funcion1 = quicksort
elif eleccion1 == 5:
    eleccion1 = "Sorted"
    funcion1 = sorted

if eleccion2 == 1:
    eleccion2 = "Bubble Sort"
    funcion2 = bubble_sort
elif eleccion2 == 2:
    eleccion2 = "Insertion Sort"
    funcion2 = insertion_sort
elif eleccion2 == 3:
    eleccion2 = "Selection Sort"
    funcion2 = selection_sort
elif eleccion2 == 4:
    eleccion2 = "Quicksort"
    funcion2 = quicksort
elif eleccion2 == 5:
    eleccion2 = "Sorted"
    funcion2 = sorted
else:
    print("Error: valor ingresado no correspondiente. Finalizando programa...")


resultadoE1_1 = medidor_de_tiempos(funcion1,lista100)
resultadoE1_2 = medidor_de_tiempos(funcion1,lista500)
resultadoE1_3 = medidor_de_tiempos(funcion1,lista1000)
resultadoE1_4 = medidor_de_tiempos(funcion1,lista5000)
resultadoE1_5 = medidor_de_tiempos(funcion1,lista10000)

resultadoE2_1 = medidor_de_tiempos(funcion2,lista100)
resultadoE2_2 = medidor_de_tiempos(funcion2,lista500)
resultadoE2_3 = medidor_de_tiempos(funcion2,lista1000)
resultadoE2_4 = medidor_de_tiempos(funcion2,lista5000)
resultadoE2_5 = medidor_de_tiempos(funcion2,lista10000)

eleccion3 = int(input("¿En qué listas quiere probar los algoritmos? \n1: Listas pequeñas (de 100 a 1000 elementos)\n2: Listas grandes y pequeñas (de 100 a 10.000 elementos)\n"))

#elecciones
if eleccion3 == 1:
    tamaños = [100, 500, 1000]
    tiempos_eleccion1 = [resultadoE1_1, resultadoE1_2, resultadoE1_3]
    tiempos_eleccion2 = [resultadoE2_1, resultadoE2_2, resultadoE2_3]
    graficar()
    print(f"Resultados de {eleccion1}: {resultadoE1_1, resultadoE1_2, resultadoE1_3}\nResultados de {eleccion2}: {resultadoE2_1, resultadoE2_2, resultadoE2_3}")
elif eleccion3 == 2:
    tamaños = [100, 500, 1000, 5000, 10000]
    tiempos_eleccion1 = [resultadoE1_1, resultadoE1_2, resultadoE1_3, resultadoE1_4, resultadoE1_5]
    tiempos_eleccion2 = [resultadoE2_1, resultadoE2_2, resultadoE2_3, resultadoE2_4, resultadoE2_5]
    graficar()
    print(f"Resultados de {eleccion1}: {resultadoE1_1, resultadoE1_2, resultadoE1_3, resultadoE1_4, resultadoE1_5}\nResultados de {eleccion2}: {resultadoE2_1, resultadoE2_2, resultadoE2_3, resultadoE2_4, resultadoE2_5}")
else:
    print("Error: valor ingresado no correspondiente. Finalizando programa...")
    
