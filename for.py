n = 10
m = 3

pecas_tirar_computador = 0

print("Computador começa!\n")

possiveisJogadas = []

for i in range(n-m, n):
    possiveisJogadas.append(i)

print(possiveisJogadas)

possiveisJogadas.reverse()

for i in possiveisJogadas:
    if i % (m+1) == 0:
        pecas_tirar_computador = i
        break

n = pecas_tirar_computador

print(n)