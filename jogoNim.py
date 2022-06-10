def computadorEscolheJogada(n: int, m: int) -> int:
    
    if n % (m+1) == 0:
        print("Você começa!\n")
        return jogadorEscolheJogada(n, m)

    else:
        print("Computador começa!\n")
        
        possiveisJogadas = []
        
        for i in range(n+1, n-m, 1):
            possiveisJogadas.append(i)

        possiveisJogadas.reverse()

        



def jogadorEscolheJogada(n: int, m: int) -> int:
    
    pecas_tirar = int(input("Quantas peças vocÊ vai tirar? \n"))

    while pecas_tirar > m:
        print("Oops! Jogada inválida! Tente de novo.\n")
        pecas_tirar = int(input("Quantas peças vocÊ vai tirar? \n"))

    n = n - pecas_tirar
    
    print(f"Você tirou {pecas_tirar} peças\n")
    
    return n


def partida():
    
    n = int(input("Quantas peças? \n"))

    m = int(input("Limite de peças por rodada? \n"))

    while n > 0:
        n = computadorEscolheJogada(n, m)
        print(f"Agora restam {n} peças no tabuleiro.\n")


partida()
