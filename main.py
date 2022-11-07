import matplotlib.pyplot as plt
import numpy as np
from time import perf_counter

def heapify(arr, n, i):
	largest = i
	l = 2 * i + 1
	r = 2 * i + 2

	if l < n and arr[i] < arr[l]:
		largest = l

	if r < n and arr[largest] < arr[r]:
		largest = r

	if largest != i:
		(arr[i], arr[largest]) = (arr[largest], arr[i])

		heapify(arr, n, largest)


def heapSort(arr):
	n = len(arr)

	for i in range(n // 2 - 1, -1, -1):
		heapify(arr, n, i)

	for i in range(n - 1, 0, -1):
		(arr[i], arr[0]) = (arr[0], arr[i])
		heapify(arr, i, 0)


arr1 = np.random.randint(1,10001,10000)
arr1R = np.arange(10000, 0, -1)

arr2 = np.random.randint(1,20001,20000)
arr2R = np.arange(20000, 0, -1)

arr3 = np.random.randint(1,40001,40000)
arr3R = np.arange(30000, 0, -1)

arr4 = np.random.randint(1,70001,70000)
arr4R = np.arange(40000, 0, -1)

arr5 = np.random.randint(1,100001,100000)
arr5R = np.arange(50000, 0, -1)

arr6 = np.random.randint(1,500001,500000)
arr6R = np.arange(80000, 0, -1)

tam = [10000, 20000, 40000, 70000, 100000, 500000]

lista = []

#array com as listas todas em ordem decrescente
listaDecrescente = []

start = perf_counter()
heapSort(arr1)
end = perf_counter()
totalTime = end - start
lista.append(totalTime)

start = perf_counter()
heapSort(arr1R)
end = perf_counter()
totalTime = end - start
listaDecrescente.append(totalTime)

start = perf_counter()
heapSort(arr2)
end = perf_counter()
totalTime = end - start
lista.append(totalTime)

start = perf_counter()
heapSort(arr2R)
end = perf_counter()
totalTime = end - start
listaDecrescente.append(totalTime)

start = perf_counter()
heapSort(arr3)
end = perf_counter()
totalTime = end - start
lista.append(totalTime)

start = perf_counter()
heapSort(arr3R)
end = perf_counter()
totalTime = end - start
listaDecrescente.append(totalTime)

start = perf_counter()
heapSort(arr4)
end = perf_counter()
totalTime = end - start
lista.append(totalTime)

start = perf_counter()
heapSort(arr4R)
end = perf_counter()
totalTime = end - start
listaDecrescente.append(totalTime)

start = perf_counter()
heapSort(arr5)
end = perf_counter()
totalTime = end - start
lista.append(totalTime)

start = perf_counter()
heapSort(arr5R)
end = perf_counter()
totalTime = end - start
listaDecrescente.append(totalTime)

start = perf_counter()
heapSort(arr6)
end = perf_counter()
totalTime = end - start
lista.append(totalTime)

start = perf_counter()
heapSort(arr6R)
end = perf_counter()
totalTime = end - start
listaDecrescente.append(totalTime)

#FALTOU COLOCAR ALGUNS LAÇOS DE REPETIÇÃO NO CÓDIGO PARA OTIMIZÁ-LO

plt.plot(tam, lista, label="Lista com números aleatórios")
plt.plot(tam, listaDecrescente, label= "Lista com números aleatórios em ordem decrescente")
plt.legend()
plt.ylabel('TEMPO (SEGUNDOS)')
plt.xlabel('TAMANHO DA LISTA')
plt.show()