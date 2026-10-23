from pathlib import Path

pasta = Path(__file__).parent

with open(pasta / "entrada.txt", "r", encoding="utf-8") as arquivo:
    entrada = arquivo.read().split()

resultados = []
i = 0

while i < len(entrada):
    n = int(entrada[i])
    f = int(entrada[i + 1])
    i += 2

    if n == 0 and f == 0:
        break

    volume = (f * 50) / 1000 / n
    resultados.append(f"{volume:.2f}")

with open(pasta / "saida.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("\n".join(resultados))
