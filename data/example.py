import sys
import random

sys.setrecursionlimit(2000000)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def shell_sort(arr):
    n = len(arr)
    gaps = [1, 5, 19, 41, 109, 209, 505, 929, 2161, 3905, 8929, 16001, 36289, 64769, 146305, 260609]
    idx = 0
    while idx < len(gaps) and gaps[idx] < n:
        idx += 1
    for gap in reversed(gaps[:idx]):
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def partition_left(arr, low, high):
    pivot = arr[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

def quick_sort_left(arr, low, high):
    if low < high:
        pi = partition_left(arr, low, high)
        quick_sort_left(arr, low, pi - 1)
        quick_sort_left(arr, pi + 1, high)
    return arr

def partition_random(arr, low, high):
    rand_pivot = random.randint(low, high)
    arr[low], arr[rand_pivot] = arr[rand_pivot], arr[low]
    return partition_left(arr, low, high)

def quick_sort_random(arr, low, high):
    if low < high:
        pi = partition_random(arr, low, high)
        quick_sort_random(arr, low, pi - 1)
        quick_sort_random(arr, pi + 1, high)
    return arr

def sort_using_algorithm(data, algorithm):
    if algorithm == 1:
        return insertion_sort(data)
    elif algorithm == 2:
        return shell_sort(data)
    elif algorithm == 3:
        return selection_sort(data)
    elif algorithm == 4:
        return heap_sort(data)
    elif algorithm == 5:
        return quick_sort_left(data, 0, len(data) - 1)
    elif algorithm == 6:
        return quick_sort_random(data, 0, len(data) - 1)
    else:
        print("Błąd: Nieprawidłowy wybór algorytmu")
        sys.exit(1)

def main():
    if len(sys.argv) == 3 and sys.argv[1] == "--algorithm":
        algorithm_number = int(sys.argv[2])
        input_data = sys.stdin.read().split()
        try:
            data = [int(x) for x in input_data[1:]]
        except EOFError:
            sys.exit(1)
        
        sorted_data = sort_using_algorithm(data, algorithm_number)
        print("Sorted data:", sorted_data[0:10])
    else:
        print("1. Insertion sort")
        print("2. Shell sort")
        print("3. Selection sort")
        print("4. Heap sort")
        print("5. Quick sort (left pivot)")
        print("6. Quick sort (random pivot)")
        algo_num = int(input("Wybierz algorytm: "))
        
        print("Wybierz rodzaj ciagu wejsciowego:")
        print("1. Losowy")
        print("2. Rosnacy")
        print("3. Malejacy")
        print("4. Staly")
        print("5. A-ksztaltny")
        seq_num = int(input("Twoj wybor ciagu: "))
        
        n = int(input("Podaj rozmiar tablicy n: "))
        
        if seq_num == 1:
            data = [random.randint(1, 1000) for _ in range(n)]
        elif seq_num == 2:
            data = list(range(n))
        elif seq_num == 3:
            data = list(range(n, 0, -1))
        elif seq_num == 4:
            data = [42] * n
        elif seq_num == 5:
            half = n // 2
            data = list(range(half)) + list(range(n - half, 0, -1))
        else:
            data = [random.randint(1, 1000) for _ in range(n)]

        print("Tablica przed sortowaniem:")
        print(data)
        
        sorted_data = sort_using_algorithm(data, algo_num)
        
        print("Tablica po sortowaniu:")
        print(sorted_data)

if __name__ == "__main__":
    main()
