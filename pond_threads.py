import time 
import _thread

# Define uma função que calcula a soma dos elementos de uma lista e armazena o resultado em uma lista de resultados
def calcular_soma(lista, resultados, index):
    soma_parcial= 0
    for num in lista:
        soma_parcial += num
    resultados[index] = soma_parcial

# Inicializa listas vazias
lista_numeros = []
lista_numeros_1= []
lista_numeros_2= []

# Preenche a lista 'lista_numeros' com números de 1 a 100
for i in range(1, 101):
    lista_numeros.append(i)

# Calcula o meio da lista para dividir em duas partes
meio_lista= len(lista_numeros) // 2

# Divide a lista manualmente em duas partes
for i in range(len(lista_numeros)):
    if (i < len(lista_numeros) / 2):
        lista_numeros_1.append(lista_numeros[i])
    else:
        lista_numeros_2.append(lista_numeros[i])

# Inicializa uma lista de resultados com duas posições, uma para cada thread
resultados = [0, 0]

# Inicia duas threads que executam a função 'calcular_soma' para cada metade da lista
_thread.start_new_thread(calcular_soma, (lista_numeros_1, resultados, 0))
_thread.start_new_thread(calcular_soma, (lista_numeros_2, resultados, 1))

# Pausa a execução por 1 segundo para garantir que as threads terminem 
time.sleep(1)

# Calcula a soma total somando os resultados parciais de ambas as threads
soma_total= sum(resultados)

print("Soma total: ", soma_total)