import random
import unittest
import pequeno_mundo as pm

class RandomTestPequenoMundo(unittest.TestCase):
    def setUp(self):
        self.n = random.randint(10, 3000)
        self.k = random.randint(1, min(10, self.n))
        self.p = round(random.uniform(0, 1), 2)
        self.peso_min = random.uniform(1.0, 5.0)
        self.peso_max = random.uniform(self.peso_min, 10.0)
        self.origem = random.randint(0, self.n-1)
        self.destino = random.randint(0, self.n-1)
        while self.destino == self.origem:
            self.destino = random.randint(0, self.n-1)
        self.rede = self.gerar_e_testar_rede()
        
        # Imprime os parâmetros de entrada para cada teste
        print("[DEBUG] n =", self.n, ", k =", self.k, ", p =", self.p,
              ", peso_min =", self.peso_min, ", peso_max =", self.peso_max,
              ", origem =", self.origem, ", destino =", self.destino)

    def gerar_e_testar_rede(self):
        rede = pm.gerar_rede_pequeno_mundo(self.n, self.k, self.p, self.peso_min, self.peso_max)
        
        # Teste: a rede tem o número correto de nós?
        self.assertEqual(len(rede.nodes()), self.n)
        
        # Teste: a rede tem o número correto de arestas?
        max_arestas = self.n * self.k // 2  
        self.assertLessEqual(len(rede.edges()), max_arestas)

        return rede

    def test_busca_em_largura_rede(self):
        caminho = pm.busca_em_largura_rede(self.rede, self.origem, self.destino)
        
        # Teste: O caminho começa e termina nos nós corretos?
        if caminho is not None:
            self.assertEqual(caminho[0][0], self.origem)
            self.assertEqual(caminho[-1][-1], self.destino)

unittest.main()
