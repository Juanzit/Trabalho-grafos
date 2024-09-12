## Algoritmo Hopcroft-Karp para correspondências máximas

Este código implementa o algoritmo Hopcroft-Karp para encontrar correspondências máximas em grafos bipartidos. Ele também inclui uma função para converter grafos direcionados em grafos bipartidos.

### Referências

* Hopcroft, J. E., & Karp, R. M. (1973). An n5/2 algorithm for maximum matchings in bipartite graphs.
* Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to algorithms. MIT press.
* Zhang, X., Han, J., & Zhang, W. (2017). An efficient algorithm for finding all possible input nodes for controlling complex networks. Scientific Reports, 7(1), 10677. 
* DELFINO, G. G. Emparelhamentos em grafos: algoritmos e implementações. 2017. 124 f. Trabalho de Conclusão de Curso (Ciência da Computação) - Instituto de Matemática e Estatística, Universidade de São Paulo, São Paulo, 2017. 

### Detalhes da implementação

* **Classe BipartiteGraph:** Representa um grafo bipartido usando uma lista de adjacência.
* **Método hopcroft_karp:** Implementa o algoritmo Hopcroft-Karp.
* **função directed_to_bipartite:** Converte um grafo direcionado em um grafo bipartido.
* **função find_possible_input_nodes:** Encontra vértices sem arestas de entrada.

### Referência do GitHub

A implementação do algoritmo Hopcroft-Karp usado como referência pode ser encontrada em [https://github.com/gidelfino/MAC0499/tree/master].
