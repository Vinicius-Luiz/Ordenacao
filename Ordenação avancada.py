'''
C(N) = Numero de comparacoes
M(N) = Numero de trocas 
A(N) = Memoria adicional
'''

'''Merge sort
Dividir um vetor em duas metades
Ordenar cada uma das metades (recursivamente)
Combinar as metadeds para formar o vetor ordenado
'''
def merge(v, esquerda, meio, direita):
    i = esquerda
    j = meio+1
    for k in range(esquerda, direita+1):
        aux[k] = v[k]
    for k in range(esquerda, direita+1):
        if i > meio:
            v[k] = aux[j]
            j += 1
        elif j > direita:
            v[k] = aux[i]
            i += 1
        elif aux[i] > aux[j]:
            v[k] = aux[j]
            j += 1
        else:
            v[k] = aux[i]
            i += 1

def TD_mergesort(v, esquerda, direita):
    if esquerda >= direita:
        return
    meio = (esquerda+direita)//2
    TD_mergesort(v, esquerda, meio)
    TD_mergesort(v, meio+1, direita)
    merge(v, esquerda, meio, direita)
    

def mergesort(v):
    N = len(v)
    global aux
    aux = []
    for x in range(N):
        aux.append(None)
    TD_mergesort(v, 0, N-1)
    del aux
    return v


'''Quicksort
Algoritmos mais importantes da engenharia e ciencia
Ideia similar ao Merge, contudo nao requer espaço adicional de armazenamento além da pilha de execução
Dividir para conquistar
Vetor é partido em 2 subvevtores conforme um elemento qlqr chamado de pivô
Esq contem elementos menores que o pivô
Dir    ''     ''     maiores  '' '  ''
-
C(N) = O(N^2) - Pior caso
C(N) = O(N lg N) - Melhor caso
C(N) = ~1,39*N lg(N) - Médio caso / O algoritmo faz apenas 39% mais comparações que no melhor caso quando aleatórizado
Para evitar o pior caso, escolhe-se um pivô aleatório dentro da sequência de índices
'''
def trocar(v, i, j):
    temp = v[i]
    v[i] = v[j]
    v[j] = temp
    
def particao(v, esquerda, direita):
    pivo = v[esquerda]
    i, j = esquerda, direita+1
    while True:
        i += 1
        while v[i] < pivo:
            if i >= direita:
                break
            i += 1
        j -= 1
        while v[j] > pivo:
            if j <= esquerda:
                break
            j -= 1
        if i >= j:
            break
        trocar(v,i,j)
    trocar(v,esquerda,j)
    print(v)
    return j

def qs (v, esquerda, direita):
    if esquerda >= direita:
        return
    p = particao(v, esquerda, direita)
    qs(v, esquerda, p-1)
    qs(v, p+1, direita)

def quicksort(v):
    N = len(v)
    qs(v, 0, N-1)
    return v
    
v = [10,40,20,30,90,2,3,6,100, 65, 12, 56, 13, 577, 1] 
print(quicksort(v))

    
                
