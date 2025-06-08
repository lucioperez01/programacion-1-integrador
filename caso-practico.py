import matplotlib.pyplot as plt
import random

# elegir el algoritmo a comparar

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


lista = [random.randint(1, 10000) for i in range(1000)]
random.randint(0,10000)



# Datos simulados: cantidad de elementos y tiempo de ejecución en segundos
tamaños = [100, 500, 1000, 5000, 10000]
tiempos_bubble = [0.01, 0.3, 1.2, 30, 120]
tiempos_merge = [0.005, 0.02, 0.05, 0.3, 1.1]

# Graficar
plt.plot(tamaños, tiempos_bubble, label="Bubble Sort", color="red", marker="o")
plt.plot(tamaños, tiempos_merge, label="Merge Sort", color="blue", marker="s")

# Etiquetas
plt.title("Comparación de Algoritmos de Ordenamiento")
plt.xlabel("Cantidad de elementos")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
