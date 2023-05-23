import networkx as nx
import random
import matplotlib.pyplot as plt

#Gera rede Pequeno Mundo com peso aleatório
def gerar_rede_pequeno_mundo(n, k, p, peso_min, peso_max):
    # Cria um rede de anel regular com k vizinhos para cada vértice
    rede = nx.random_regular_graph(k, n)


    # Adiciona pesos aleatórios às arestas
    for (u, v) in rede.edges():
        peso = random.uniform(peso_min, peso_max)
        rede.edges[u, v]['weight'] = peso
    # Reconecta as arestas com probabilidade p
    for u in rede.nodes():
        for v in list(rede[u]):
            if random.random() < p:
                w = random.choice(list(rede.nodes()))
                while w == u or rede.has_edge(u, w):
                    w = random.choice(list(rede.nodes()))
                rede.remove_edge(u, v)
                rede.add_edge(u, w, weight=random.uniform(peso_min, peso_max))
                
    return rede

#busca em largura
def busca_em_largura_rede(rede, origem, destino):
    try:
        caminho = nx.shortest_path(rede, origem, destino)
        caminho_percurso = [(caminho[i], caminho[i+1]) for i in range(len(caminho)-1)]
        imprime_rede(rede)
        print("Caminho percorrido da origem ao destino:")
        for u, v in caminho_percurso:
            print(u, "->", v)
        return caminho_percurso
    except nx.NetworkXNoPath:
        print("Não foi encontrado um caminho da origem ao destino.")
        imprime_rede(rede)
        return None

def imprime_rede(rede):
    # Imprime a rede gerada
    print("Vértices: ", rede.nodes())
    print("Arestas: ", rede.edges())

    nx.draw(rede)
    nx.draw_circular(rede, with_labels=True)
    plt.show()