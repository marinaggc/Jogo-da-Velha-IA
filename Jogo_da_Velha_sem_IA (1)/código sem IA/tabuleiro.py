# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [
            [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
            [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
            [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]
        ]

    def exibir(self):
        simbolos = {
            Tabuleiro.DESCONHECIDO: " ",
            Tabuleiro.JOGADOR_0: "O",
            Tabuleiro.JOGADOR_X: "X"
        }
        for linha in self.matriz:
            print("|".join(simbolos[celula] for celula in linha))
            print("-" * 5)

    def jogada_valida(self, linha, coluna):
        return self.matriz[linha][coluna] == Tabuleiro.DESCONHECIDO

    def fazer_jogada(self, linha, coluna, jogador):
        if self.jogada_valida(linha, coluna):
            self.matriz[linha][coluna] = jogador
            return True
        else:
            print("Jogada inválida! Tente novamente.")
            return False

    def tem_campeao(self):
        # Checa linhas
        for linha in self.matriz:
            if linha[0] != Tabuleiro.DESCONHECIDO and linha[0] == linha[1] == linha[2]:
                return linha[0]

        # Checa colunas
        for col in range(3):
            if (self.matriz[0][col] != Tabuleiro.DESCONHECIDO and
                self.matriz[0][col] == self.matriz[1][col] == self.matriz[2][col]):
                return self.matriz[0][col]

        # Checa diagonal principal
        if (self.matriz[0][0] != Tabuleiro.DESCONHECIDO and
            self.matriz[0][0] == self.matriz[1][1] == self.matriz[2][2]):
            return self.matriz[0][0]

        # Checa diagonal secundária
        if (self.matriz[0][2] != Tabuleiro.DESCONHECIDO and
            self.matriz[0][2] == self.matriz[1][1] == self.matriz[2][0]):
            return self.matriz[0][2]

        return Tabuleiro.DESCONHECIDO

    def empate(self):
        for linha in self.matriz:
            if Tabuleiro.DESCONHECIDO in linha:
                return False
        return self.campeao() == Tabuleiro.DESCONHECIDO

# Exemplo de uso simples:
if __name__ == "__main__":
    jogo = Tabuleiro()
    jogador_atual = Tabuleiro.JOGADOR_X

    while True:
        jogo.exibir()
        print(f"Jogador {'X' if jogador_atual == Tabuleiro.JOGADOR_X else 'O'}:")
        try:
            linha = int(input("Linha (0-2): "))
            coluna = int(input("Coluna (0-2): "))
        except ValueError:
            print("Entrada inválida! Use números entre 0 e 2.")
            continue

        if not (0 <= linha <= 2 and 0 <= coluna <= 2):
            print("Fora do tabuleiro! Tente novamente.")
            continue

        if jogo.fazer_jogada(linha, coluna, jogador_atual):
            vencedor = jogo.campeao()
            if vencedor != Tabuleiro.DESCONHECIDO:
                jogo.exibir()
                print(f"Jogador {'X' if vencedor == Tabuleiro.JOGADOR_X else 'O'} venceu!")
                break
            elif jogo.empate():
                jogo.exibir()
                print("Empate!")
                break
            jogador_atual = Tabuleiro.JOGADOR_O if jogador_atual == Tabuleiro.JOGADOR_X else Tabuleiro.JOGADOR_X
