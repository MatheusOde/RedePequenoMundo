import unittest
import pequeno_mundo as pm


class TestPequenoMundo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.n = 20
        cls.k = 3
        cls.p = 0.2
        cls.peso_min = 1.0
        cls.peso_max = 10.0
        cls.origem = 5
        cls.destino = 2
        cls.rede = pm.gerar_rede_pequeno_mundo(
            cls.n, cls.k, cls.p, cls.peso_min, cls.peso_max)

    def test_rede_pequeno_mundo(self):
        # Teste: a rede tem o número correto de nós?
        self.assertEqual(len(self.rede.nodes()), self.n)

        # Teste: a rede tem o número correto de arestas?
        max_arestas = self.n * self.k // 2
        self.assertLessEqual(len(self.rede.edges()), max_arestas)

    def test_busca_em_largura_rede(self):
        caminho = pm.busca_em_largura_rede(
            self.rede, self.origem, self.destino)

        # Teste: O caminho começa e termina nos nós corretos?
        if caminho is not None:
            self.assertEqual(caminho[0][0], self.origem)
            self.assertEqual(caminho[-1][-1], self.destino)

    def test_busca_em_profundidade_rede(self):
        caminho = pm.busca_em_profundidade_rede(
            self.rede, self.origem, self.destino)

        # Teste: O caminho começa e termina nos nós corretos?
        if caminho is not None:
            self.assertEqual(caminho[0][0], self.origem)
            self.assertEqual(caminho[-1][-1], self.destino)

    def test_busca_best_first_rede(self):
        caminho = pm.busca_best_first_search_rede(
            self.rede, self.origem, self.destino)

        # Teste: O caminho começa e termina nos nós corretos?
        if caminho is not None:
            self.assertEqual(caminho[0][0], self.origem)
            self.assertEqual(caminho[-1][-1], self.destino)

    def test_busca_a_estrela_rede(self):
        caminho = pm.busca_a_estrela_rede(
            self.rede, self.origem, self.destino)

        # Teste: O caminho começa e termina nos nós corretos?
        if caminho is not None:
            self.assertEqual(caminho[0][0], self.origem)
            self.assertEqual(caminho[-1][-1], self.destino)

    def test_busca_dijkstra_rede(self):
        caminho = pm.busca_dijkstra(
            self.rede, self.origem, self.destino)

        # Teste: O caminho começa e termina nos nós corretos?
        if caminho is not None:
            self.assertEqual(caminho[0][0], self.origem)
            self.assertEqual(caminho[-1][-1], self.destino)


unittest.main(exit=False)
pm.imprime_rede(TestPequenoMundo.rede)
