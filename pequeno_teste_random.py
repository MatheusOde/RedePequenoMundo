import random
import unittest
import pequeno_mundo as pm


class RandomTestPequenoMundo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.n = random.randint(10, 3000)
        cls.k = random.randint(1, min(10, cls.n))
        cls.p = round(random.uniform(0, 1), 2)
        cls.peso_min = random.uniform(1.0, 5.0)
        cls.peso_max = random.uniform(cls.peso_min, 10.0)
        cls.origem = random.randint(0, cls.n-1)
        cls.destino = random.randint(0, cls.n-1)
        while cls.destino == cls.origem:
            cls.destino = random.randint(0, cls.n-1)
        cls.rede = pm.gerar_rede_pequeno_mundo(
            cls.n, cls.k, cls.p, cls.peso_min, cls.peso_max)

        # Imprime os parâmetros de entrada para cada teste
        print("[DEBUG] n =", cls.n, ", k =", cls.k, ", p =", cls.p,
              ", peso_min =", cls.peso_min, ", peso_max =", cls.peso_max,
              ", origem =", cls.origem, ", destino =", cls.destino)

    @classmethod
    def test_rede_pequeno_mundo(cls):

        # Teste: a rede tem o número correto de nós?
        assert len(cls.rede.nodes()) == cls.n

        # Teste: a rede tem o número correto de arestas?
        max_arestas = cls.n * cls.k // 2
        assert len(cls.rede.edges()) <= max_arestas

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
pm.imprime_rede(RandomTestPequenoMundo.rede)
