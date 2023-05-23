import unittest
import pequeno_mundo as pm

class TestPequenoMundo(unittest.TestCase):
    def setUp(self):
        self.n = 20  
        self.k = 4 
        self.p = 0.2  
        self.peso_min = 1.0 
        self.peso_max = 10.0 
        self.origem = 5
        self.destino = 2
        self.rede = pm.gerar_rede_pequeno_mundo(self.n, self.k, self.p, self.peso_min, self.peso_max)

    def test_gerar_rede_pequeno_mundo(self):
        # Teste: a rede tem o número correto de nós?
        self.assertEqual(len(self.rede.nodes()), self.n)
        
        # Teste: a rede tem o número correto de arestas?
        max_arestas = self.n * self.k // 2  
        self.assertLessEqual(len(self.rede.edges()), max_arestas)

    def test_busca_em_largura_rede(self):
        caminho = pm.busca_em_largura_rede(self.rede, self.origem, self.destino)
        
        # Teste: O caminho começa e termina nos nós corretos?
        if caminho is not None:
            self.assertEqual(caminho[0][0], self.origem)
            self.assertEqual(caminho[-1][-1], self.destino)

unittest.main()