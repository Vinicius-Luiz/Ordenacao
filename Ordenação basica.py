'''
C(N) = Numero de comparacoes
M(N) = Numero de trocas 
A(N) = Memoria adicional
'''
def trocar(v, i, j):
    temp = v[i]
    v[i] = v[j]
    v[j] = temp

'''Bubble sort
Repetidas trocas entre elementos consecutivos
Se elemento maior que proximo, trocar
Elementos maiores 'flutuam' em direção ao fim do vetor
-
C(N) = O(N^2)
M(N) = O(N^2)
Péssimo desempenho
Estável
Custo independe se o vetor está (parcialmente) ordenado
Uso para poucos itens'''
def bubblesort(v):
    N = len(v)
    for i in range (N-1, -1, -1):
        for j in range(0, i):
            #print(i,j)
            if v[j] > v[j+1]:
                trocar(v, j, j+1)
        print(v)
    print(v)


'''Selection sort
encontrar menor elemento do vetor
trocá-lo com o primeiro elemento
desconsiderar menor elemento
repetir processo para os demais
-
C(N) = O(N^2)
M(N) = O(N)
Simples de implementar
Poucas trocas (útil para casos em que os itens são grandes)
Não estável
Custo independe se vetor está (parcialmente) ordenado'''
def selectionsort(v):
    N = len(v)
    for i in range(N):
        minimo = i
        for j in range(i+1, N):
            #print(i,j)
            if v[minimo] > v[j]:
                minimo = j
        trocar(v,i,minimo)
        print(v)
    print(v)


'''Insertion sort
Dividir vetor entre ordenados (à esquerda) e a ordenar (à direita)
Inserir primeiro elemento da direita na subsequência ordenada da esquerda
Repetir processo até que todos tenham sido avaliados
Processo similar a ordernar cartas na mão
-
Melhor caso: Elemento encontra-se na posição correta: 1 única
C(N) = O(N)
M(N) = O(N)

Pior caso:
C(N) = O(N^2)
M(N) = O(N^2)'''
def insertionsort(v):
    N = len(v)
    for i in range(N):
        aux = v[i]
        j = i-1
        while j >= 0 and v[j] > aux:
            v[j+1] = v[j]
            j -= 1
        v[j+1] = aux
    print(v)
    

'''Shell sort
O maor número de movimentações do método por inserção e quando o menor elemento enconotra-se mais à direita
Este método resolve esse problema trocando elementos com posições mais distantes
Formam-se subsequências ordenadas entre elementos separados por h posições
Em seguida, diminui-se o valor de h e o processo é repetido até h=1
-
Complexidade depende da sequência escolhida
Bom desempenho para vetor de tamanhos moderados, mas e inferior a outros algoritmos
Pode ocorrer muitos cache misses (n sei explicar) - pode piorar desempenho em PC's modernos
'''
def shellsort(v):
    N = len(v)
    h = 1
    while h < N//3:
        h = 3*h+1
    while h >= 1:
        for i in range(h, N):
            j = i
            while j>= h and v[j] < v[j-h]:
                trocar(v, j, j-h)
                j -= h
                print(v)
        h //= 3


v = [4,6,7,1,2,3,9,8,10,5]
print(v)
shellsort(v)


    
