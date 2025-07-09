# -*- coding: utf-8 -*- 
from typing import Tuple
from jogador import Jogador
from tabuleiro import Tabuleiro
from random import choice 

class JogadorIA(Jogador):
    def __init__(self, tabuleiro: Tabuleiro, tipo: int):
        super().__init__(tabuleiro, tipo)

    def getJogada(self) -> Tuple[(int, int)]:
        matriz = self.matriz
        adversario = Tabuleiro.JOGADOR_X if self.tipo == Tabuleiro.JOGADOR_0 else Tabuleiro.JOGADOR_0

        # R1 - Ganhar ou bloquear
        def linha_coluna_diagonal_vitoria(tipo):
            for i in range(3):
                # Linhas
                if matriz[i].count(tipo) == 2 and matriz[i].count(Tabuleiro.DESCONHECIDO) == 1:
                    return (i, matriz[i].index(Tabuleiro.DESCONHECIDO))
                # Colunas
                col = [matriz[0][i], matriz[1][i], matriz[2][i]]
                if col.count(tipo) == 2 and col.count(Tabuleiro.DESCONHECIDO) == 1:
                    return (col.index(Tabuleiro.DESCONHECIDO), i)
            # Diagonal principal
            diag = [matriz[i][i] for i in range(3)]
            if diag.count(tipo) == 2 and diag.count(Tabuleiro.DESCONHECIDO) == 1:
                idx = diag.index(Tabuleiro.DESCONHECIDO)
                return (idx, idx)
            # Diagonal secundária
            anti = [matriz[i][2 - i] for i in range(3)]
            if anti.count(tipo) == 2 and anti.count(Tabuleiro.DESCONHECIDO) == 1:
                idx = anti.index(Tabuleiro.DESCONHECIDO)
                return (idx, 2 - idx)
            return None

        # R1 - Tente ganhar ou bloquear o adversário
        for t in [self.tipo, adversario]:
            jogada = linha_coluna_diagonal_vitoria(t)
            if jogada:
                return jogada

        # R2 - Criar duas ameaças (duas sequências de 2)
        def conta_duplas(tipo, linha, coluna):
            matriz[linha][coluna] = tipo
            count = 0
            if matriz[linha].count(tipo) == 2 and matriz[linha].count(Tabuleiro.DESCONHECIDO) == 1:
                count += 1
            col = [matriz[i][coluna] for i in range(3)]
            if col.count(tipo) == 2 and col.count(Tabuleiro.DESCONHECIDO) == 1:
                count += 1
            if linha == coluna:
                diag = [matriz[i][i] for i in range(3)]
                if diag.count(tipo) == 2 and diag.count(Tabuleiro.DESCONHECIDO) == 1:
                    count += 1
            if linha + coluna == 2:
                anti = [matriz[i][2 - i] for i in range(3)]
                if anti.count(tipo) == 2 and anti.count(Tabuleiro.DESCONHECIDO) == 1:
                    count += 1
            matriz[linha][coluna] = Tabuleiro.DESCONHECIDO
            return count

        melhores = []
        for l in range(3):
            for c in range(3):
                if matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    if conta_duplas(self.tipo, l, c) >= 2:
                        melhores.append((l, c))
        if melhores:
            return melhores[0]

        # R3 - Centro livre
        if matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)

        # R4 - Canto oposto
        cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
        opostos = {(0, 0): (2, 2), (0, 2): (2, 0), (2, 0): (0, 2), (2, 2): (0, 0)}
        for canto in cantos:
            if matriz[canto[0]][canto[1]] == adversario:
                oposto = opostos[canto]
                if matriz[oposto[0]][oposto[1]] == Tabuleiro.DESCONHECIDO:
                    return oposto

        # R5 - Canto livre
        for canto in cantos:
            if matriz[canto[0]][canto[1]] == Tabuleiro.DESCONHECIDO:
                return canto

        # R6 - Qualquer posição
        for l in range(3):
            for c in range(3):
                if matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    return (l, c)

        return None
