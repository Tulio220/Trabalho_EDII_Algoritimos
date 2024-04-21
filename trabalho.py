import requests
import time
import copy

# Função para obter a lista de cidades da API do IBGE
def get_city_list():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        cities = [city['nome'] for city in data]  # Extrair apenas os nomes das cidades
        return cities
    else:
        print("Erro ao obter a lista de cidades.")
        return None

# Algoritmo de ordenação: Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Algoritmo de ordenação: Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Algoritmo de ordenação: Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Algoritmo de ordenação: Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Algoritmo de ordenação: Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)

# Função para medir o tempo de execução de um algoritmo de ordenação
def measure_sorting_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

# Obter a lista de cidades
cities = get_city_list()

# Copiar a lista para que cada algoritmo de ordenação comece com a mesma lista desordenada
cities_copy = copy.deepcopy(cities)

# Medir o tempo de execução de cada algoritmo de ordenação
algorithms = {
    "Insertion Sort": insertion_sort,
    "Selection Sort": selection_sort,
    "Bubble Sort": bubble_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort
}

results = {}

for algorithm_name, sort_function in algorithms.items():
    cities_copy = copy.deepcopy(cities)
    execution_time = measure_sorting_time(sort_function, cities_copy)
    results[algorithm_name] = execution_time

# Imprimir resultados
print("Resultados:")
print("{:<15} {:<15}".format("Algoritmo", "Tempo de Execução (s)"))
for algorithm_name, execution_time in results.items():
    print("{:<15} {:<15.6f}".format(algorithm_name, execution_time))
