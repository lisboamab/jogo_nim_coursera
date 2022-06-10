def computadorEscolheJogada(n: int, m: int):
    pass

def jogadorEscolheJogada(n: int, m: int):
    pecas_tirar = int(input("Quantas peças vocÊ vai tirar? "))

    while pecas_tirar > m:
        print("Oops! Jogada inválida! Tente de novo.")
        pecas_tirar = int(input("Quantas peças vocÊ vai tirar? "))

    n = n - pecas_tirar

    return n
def partida():
    n = int(input("Quantas peças? "))

    m = int(input("Limite de peças por rodada? "))



jogadorEscolheJogada(10, 1)