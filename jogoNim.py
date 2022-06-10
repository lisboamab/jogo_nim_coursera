def computadorEscolheJogada(n: int, m: int) -> int:
    
    pecas_tirar_computador = 0

    if n % (m+1) == 0:
        print("Você começa!\n")
        return jogadorEscolheJogada(n, m)

    else:
        print("Computador começa!\n")
        
        possiveisJogadas = []
        
        for i in range(n-m, n):
            possiveisJogadas.append(i)

        possiveisJogadas.reverse()

        for i in possiveisJogadas:
            if i % (m+1) == 0:
                pecas_tirar_computador = i
                break
        
        n = pecas_tirar_computador

        possiveisJogadas.clear()
        
        return n


def jogadorEscolheJogada(n: int, m: int) -> int:
    
    pecas_tirar = int(input("Quantas peças você vai tirar? \n"))

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
