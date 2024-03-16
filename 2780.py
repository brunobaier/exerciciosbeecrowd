
pontos = 0

lancamentosDistancia = int(input())

if lancamentosDistancia <= 800:
    pontos = 1
elif lancamentosDistancia > 800 and lancamentosDistancia <= 1400:
    pontos = 2
elif lancamentosDistancia > 1400 and  lancamentosDistancia <= 2000:
    pontos = 3

print(pontos)