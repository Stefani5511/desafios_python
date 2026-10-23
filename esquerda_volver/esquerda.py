from pathlib import Path

pasta = Path(__file__).parent

with open(pasta / "entrada.txt", "r", encoding="utf-8") as arquivo:
    entrada = arquivo.read().split()

resultados = []
direcoes = ["N", "L", "S", "O"]
i = 0

while i < len(entrada):
    n = int(entrada[i])
    i += 1

    if n == 0:
        break

    comandos = entrada[i]
    i += 1

    posicao = 0

    for comando in comandos:
        if comando == "D":
            posicao = (posicao + 1) % 4
        else:
            posicao = (posicao - 1) % 4

    resultados.append(direcoes[posicao])

with open(pasta / "saida.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("\n".join(resultados))
