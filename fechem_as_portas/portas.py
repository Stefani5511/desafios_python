from pathlib import Path
from math import isqrt

pasta = Path(__file__).parent

with open(pasta / "entrada.txt", "r", encoding="utf-8") as arquivo:
    entrada = arquivo.read().split()

resultados = []

for valor in entrada:
    n = int(valor)

    if n == 0:
        break

    portas_abertas = []

    for i in range(1, isqrt(n) + 1):
        portas_abertas.append(str(i * i))

    resultados.append(" ".join(portas_abertas))

with open(pasta / "saida.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("\n".join(resultados))
