"""

2) Em uma escola, um aluno tem sua média calculada a partir da média ponderada de três notas, sendo que a primeira nota
vale 20% da média final, a segunda vale 35% e a terceira vale 45%. Exibir a média final após os cálculos

"""
while True:
    try:
        nota1 = float(input('Digite o valor da sua PRIMEIRA nota:\n'))
        if nota1 >= 0 and nota1 <= 10:
            break
        print("\nPor favor, digite um número válido.")
    except:
        print("\nPor favor, digite um número válido.")

while True:
    try:
        nota2 = float(input('Digite o valor da sua SEGUNDA nota:\n'))
        if nota2 >= 0 and nota2 <= 10:
            break
        print("\nPor favor, digite um número válido.")
    except:
        print("\nPor favor, digite um número válido.")

while True:
    try:
        nota3 = float(input('Digite o valor da sua TERCEIRA nota:\n'))
        if nota3 >= 0 and nota3 <= 10:
            break
        print("\nPor favor, digite um número válido.")
    except:
        print("\nPor favor, digite um número válido.")

print(f"\n\t PRIMEIRA nota PONDERADA = {nota1 * 0.20:.2f}")
print(f"\t SEGUNDA nota PONDERADA = {nota2 * 0.35:.2f}")
print(f"\t TERCEIRA nota PONDERADA = {nota3 * 0.45}")
print(f"\t MÉDIA FINAL = {nota1 * 0.20 + nota2 * 0.35 + nota3 * 0.45:.2f}")

nota1 = 0
nota2 = 0
nota3 = 0