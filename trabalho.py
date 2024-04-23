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

# Variável global para contar comparações
comparisons = 0

# Algoritmo de ordenação: Insertion Sort
def insertion_sort(arr):
    global comparisons
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Algoritmo de ordenação: Selection Sort
def selection_sort(arr):
    global comparisons
    comparisons = 0
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Algoritmo de ordenação: Bubble Sort
def bubble_sort(arr):
    global comparisons
    comparisons = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Algoritmo de ordenação: Merge Sort
def merge_sort(arr):
    global comparisons
    comparisons = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            comparisons += 1
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
    global comparisons
    comparisons = 0
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        comparisons += len(lesser) + len(greater)
        return quick_sort(lesser) + [pivot] + quick_sort(greater)

# Função para medir o tempo de execução de um algoritmo de ordenação
def measure_sorting_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

# Função para medir o tempo de execução e contar comparações
def measure_sorting_time_and_comparisons(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    execution_time = end_time - start_time
    global comparisons
    num_comparisons = comparisons
    return execution_time, num_comparisons

# Obter a lista de cidades
cities = get_city_list()

# Copiar a lista para que cada algoritmo de ordenação comece com a mesma lista desordenada
cities_copy = copy.deepcopy(cities)

# Medir o tempo de execução e o número de comparações de cada algoritmo de ordenação
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
    execution_time, num_comparisons = measure_sorting_time_and_comparisons(sort_function, cities_copy)
    results[algorithm_name] = {'execution_time': execution_time, 'num_comparisons': num_comparisons}

# Imprimir resultados
print("Resultados:")
print("{:<15} {:<20} {:<30}".format("Algoritmo", "Tempo de Execução (s)", "Número de Comparações"))
for algorithm_name, metrics in results.items():
    print("{:<15} {:<20.6f} {:<30}".format(algorithm_name, metrics['execution_time'], metrics['num_comparisons']))
