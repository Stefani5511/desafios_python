from pathlib import Path

pasta = Path(__file__).parent

with open(pasta / "entrada.txt", "r", encoding="utf-8") as arquivo:
    entrada = arquivo.read().splitlines()

resultados = []
i = 0

while i < len(entrada):
    n = int(entrada[i].strip())
    i += 1

    if n == 0:
        break

    erros = {}
    resolvidos = set()
    problemas_resolvidos = 0
    penalidade_total = 0

    for _ in range(n):
        problema, tempo, julgamento = entrada[i].split()
        i += 1

        tempo = int(tempo)

        if problema in resolvidos:
            continue

        if julgamento == "incorrect":
            erros[problema] = erros.get(problema, 0) + 1

        elif julgamento == "correct":
            resolvidos.add(problema)
            problemas_resolvidos += 1
            penalidade_total += tempo
            penalidade_total += erros.get(problema, 0) * 20

    resultados.append(f"{problemas_resolvidos} {penalidade_total}")

with open(pasta / "saida.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("\n".join(resultados))
