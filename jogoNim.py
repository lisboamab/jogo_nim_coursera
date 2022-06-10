def computadorEscolheJogada(n: int, m: int) -> int:
    
    if n % (m+1) == 0:
        print("Você começa!")
        return jogadorEscolheJogada(n, m)

    else:
        print("Computador começa!")
        if True:
            ...
def jogadorEscolheJogada(n: int, m: int) -> int:
    pecas_tirar = int(input("Quantas peças vocÊ vai tirar? "))

    while pecas_tirar > m:
        print("Oops! Jogada inválida! Tente de novo.")
        pecas_tirar = int(input("Quantas peças vocÊ vai tirar? "))

    n = n - pecas_tirar
    print(f"Você tirou {pecas_tirar} peças")
    return n


def partida():
    n = int(input("Quantas peças? "))

    m = int(input("Limite de peças por rodada? "))

    while n > 0:
        n = computadorEscolheJogada(n, m)


partida()
