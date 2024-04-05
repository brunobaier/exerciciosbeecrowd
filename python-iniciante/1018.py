valorInteiro = int(input())

print(valorInteiro)
valorEmNotaDeCem = valorInteiro // 100
valorInteiroRestante = valorInteiro - (valorEmNotaDeCem * 100)

valorEmNotasDeCinquenta = valorInteiroRestante // 50
aux = valorInteiroRestante - (valorEmNotasDeCinquenta * 50)
valorInteiroRestante = aux

valorEmNotasDeVinte = valorInteiroRestante // 20
aux = valorInteiroRestante - (valorEmNotasDeVinte * 20)
valorInteiroRestante = aux

valorEmNotaDeDez = valorInteiroRestante // 10
aux = valorInteiroRestante - (valorEmNotaDeDez * 10)
valorInteiroRestante = aux

valorEmNotasDeCinco = valorInteiroRestante // 5
aux = valorInteiroRestante - (valorEmNotasDeCinco * 5)
valorInteiroRestante = aux

valorEmNotasDeDois = valorInteiroRestante // 2
aux = valorInteiroRestante - (valorEmNotasDeDois * 2)
valorInteiroRestante = aux

valorEmNotasDeUm = valorInteiroRestante // 1
aux = valorInteiroRestante - (valorEmNotasDeUm * 1)
valorInteiroRestante = aux


print(f"{valorEmNotaDeCem} nota(s) de R$ 100,00")
print(f"{valorEmNotasDeCinquenta} nota(s) de R$ 50,00")
print(f"{valorEmNotasDeVinte} nota(s) de R$ 20,00")
print(f"{valorEmNotaDeDez} nota(s) de R$ 10,00")
print(f"{valorEmNotasDeCinco} nota(s) de R$ 5,00")
print(f"{valorEmNotasDeDois} nota(s) de R$ 2,00")
print(f"{valorEmNotasDeUm} nota(s) de R$ 1,00")