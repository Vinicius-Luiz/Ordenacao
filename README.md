### Universidade Federal de Pernambuco (UFPE) (http://www.ufpe.br)
### Centro de Informática (CIn) (http://www.cin.ufpe.br)
### Graduando em Sistemas de Informação
### IF969 - Algoritmos e Estrutura de Dados

### Autor: Vinícius Luiz da Silva França (vlsf2)
### Email: vlsf2@cin.ufpe.br
### Data: 2020-10-14

### Copyright(c) 2020 Vinícius Luiz da Silva França

> C(N) = Numero de comparações
> M(N) = Numero de trocas 
> A(N) = Memoria adicional

> **Ordenação Básica**
>
> - Bubblesort
>
>   - Repetidas trocas entre elementos consecutivos
>     Se elemento maior que proximo, trocar
>     Elementos maiores 'flutuam' em direção ao fim do vetor
>     -
>     C(N) = O(N^2)
>     M(N) = O(N^2)
>     Péssimo desempenho
>     Estável
>     Custo independe se o vetor está (parcialmente) ordenado
>     Uso para poucos itens
>
> - Selectionsort
>
>   - encontrar menor elemento do vetor
>     trocá-lo com o primeiro elemento
>     desconsiderar menor elemento
>     repetir processo para os demais
>     -
>     C(N) = O(N^2)
>     M(N) = O(N)
>     Simples de implementar
>     Poucas trocas (útil para casos em que os itens são grandes)
>     Não estável
>     Custo independe se vetor está (parcialmente) ordenado
>
> - Insertionsort
>
>   - Dividir vetor entre ordenados (à esquerda) e a ordenar (à direita)
>     Inserir primeiro elemento da direita na subsequência ordenada da esquerda
>     Repetir processo até que todos tenham sido avaliados
>     Processo similar a ordenar cartas na mão
>     -
>     Melhor caso: Elemento encontra-se na posição correta: 1 única
>     C(N) = O(N)
>     M(N) = O(N)
>
>     Pior caso:
>     C(N) = O(N^2)
>     M(N) = O(N^2)
>
> - Shellsort
>
>   - O maior número de movimentações do método por inserção e quando o menor elemento encontra-se mais à direita
>     Este método resolve esse problema trocando elementos com posições mais distantes
>     Formam-se subsequências ordenadas entre elementos separados por h posições
>     Em seguida, diminui-se o valor de h e o processo é repetido até h=1
>     -
>     Complexidade depende da sequência escolhida
>     Bom desempenho para vetor de tamanhos moderados, mas e inferior a outros algoritmos
>     Pode ocorrer muitos cache misses (n sei explicar) - pode piorar desempenho em PC's modernos
>
> **Ordenação Avançada**
>
> - Mergesort
>   - Dividir um vetor em duas metades
>     Ordenar cada uma das metades (recursivamente)
>     Combinar as metades para formar o vetor ordenado
> - Quicksort
>   - Algoritmos mais importantes da engenharia e ciência
>     Ideia similar ao Merge, contudo não requer espaço adicional de armazenamento além da pilha de execução
>     Dividir para conquistar
>     Vetor é partido em 2 subvetores conforme um elemento qualquer chamado de pivô
>     Esq contem elementos menores que o pivô
>     Dir    ''     ''    				    maiores  '' '  ''
>     -
>     C(N) = O(N^2) - Pior caso
>     C(N) = O(N lg N) - Melhor caso
>     C(N) = ~1,39*N lg(N) - Médio caso / O algoritmo faz apenas 39% mais comparações que no melhor caso quando aleatorizado
>     Para evitar o pior caso, escolhe-se um pivô aleatório dentro da sequência de índices