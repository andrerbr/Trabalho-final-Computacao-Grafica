import numpy as np
import math


class Rasterizacao:
    def __init__(self, entrada):
        self.entrada = entrada  # lista de pontos da figura de entrada
        self.saida = []  # lista de pontos que compoem a rasterização


class Bresenham(Rasterizacao):
    def __init__(self, ponto1, ponto2):
        super().__init__([ponto1, ponto2])
        self.x1 = ponto1[0]
        self.y1 = ponto1[1]
        self.x2 = ponto2[0]
        self.y2 = ponto2[1]
        self.pontos = []
        self.troca_x = False
        self.troca_y = False
        self.troca_xy = False
        if ponto1 == ponto2:
            self.saida = [[self.x1, self.y1]]
            return
        self.checar_octante()

        x = self.x1
        y = self.y1

        delta_x = self.x2 - self.x1
        delta_y = self.y2 - self.y1

        m = delta_y / delta_x
        e = m - (1 / 2)

        self.pontos.append([x, y])

        while x < self.x2:
            if e >= 0:
                y += 1
                e -= 1
            x += 1
            e += m
            self.pontos.append([x, y])

        self.reflexao(self.pontos)
        self.saida = self.pontos

    def checar_octante(self):

        delta_x = self.x2 - self.x1
        delta_y = self.y2 - self.y1

        if delta_x != 0:
            m = delta_y / delta_x
        else:
            m = 2

        if m > 1 or m < -1:
            [self.x1, self.y1] = [self.y1, self.x1]
            [self.x2, self.y2] = [self.y2, self.x2]
            self.troca_xy = True

        if self.x1 > self.x2:
            self.x1 = -self.x1
            self.x2 = -self.x2
            self.troca_x = True

        if self.y1 > self.y2:
            self.y1 = -self.y1
            self.y2 = -self.y2
            self.troca_y = True

    def reflexao(self, pts: list):
        if self.troca_y:
            for pt in self.pontos:
                pt[1] = -pt[1]

        if self.troca_x:
            for pt in self.pontos:
                pt[0] = -pt[0]

        if self.troca_xy:
            for pt in self.pontos:
                [pt[0], pt[1]] = [pt[1], pt[0]]


class Polilinha(Rasterizacao):
    def __init__(self, pontos: list, fechar=False):
        super().__init__(pontos)

        if fechar:
            pontos.append(pontos[0])

        for x in range(len(pontos) - 1):
            linha = Bresenham(pontos[x], pontos[x + 1])

            for pt in linha.saida:
                self.saida.append(pt)


class Projection(Rasterizacao):
    def __init__(self, entrada, recuo):
        for coordenada in entrada:
            coordenada[2] += recuo
        super().__init__(entrada)

    def ortogonal(self):
        for ponto in self.entrada:
            ponto.append(1)

        matriz_proj = [
            [0 for i in range(len(self.entrada[0]))]
            for i in range(len(self.entrada[0]))
        ]

        missed_diagonal = 2
        x_saida = 0
        y_saida = 1

        for i in range(0, len(self.entrada[0])):
            if i != missed_diagonal:
                matriz_proj[i][i] = 1

        for point in self.entrada:
            projecao = np.dot(matriz_proj, point)
            self.saida.append([projecao[x_saida], projecao[y_saida]])

    def perspectiva(self, dist):
        for ponto in self.entrada:
            ponto.append(1)

        matriz_perspectiva = [
            [0 for i in range(len(self.entrada[0]))]
            for i in range(len(self.entrada[0]))
        ]

        for i in range(0, len(self.entrada[0])):
            if i != len(self.entrada[0]) - 1:
                matriz_perspectiva[i][i] = dist

        matriz_perspectiva[len(matriz_perspectiva) - 1][len(matriz_perspectiva) - 2] = 1

        for point in self.entrada:
            projecao = np.dot(matriz_perspectiva, point)
            projecao = np.multiply(projecao, 1 / point[2])
            self.saida.append([round(projecao[0]), round(projecao[1])])

    def _oblique(self, L, alpha_deg=45):
        """
        Calcula uma projeção oblíqua genérica.
        L=1 para Cavalier, L=0.5 para Cabinet.
        """
        alpha_rad = math.radians(alpha_deg)
        for ponto in self.entrada:
            ponto.append(1)

        # Matriz de projeção oblíqua
        matriz_proj = np.array([
            [1, 0, L * math.cos(alpha_rad), 0],
            [0, 1, L * math.sin(alpha_rad), 0],
            [0, 0, 0, 0],
            [0, 0, 0, 1]
        ])

        for point in self.entrada:
            projecao = np.dot(matriz_proj, point)
            self.saida.append([round(projecao[0]), round(projecao[1])])

    def cavalier(self, alpha_deg=45):
        self._oblique(L=1, alpha_deg=alpha_deg)

    def cabinet(self, alpha_deg=45):
        self._oblique(L=0.5, alpha_deg=alpha_deg)
