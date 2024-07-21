"""

4) Solicitar a idade de uma pessoa em anos, meses e dias; calcule e mostre a idade expressa apenas em dias.
Obs: Considere arredondar o ano para 365 dias e os mêses para exatos 30 dias.

"""
while True:
    while True:
        try:
            anosVividos = int(input('Qual o seu total de ANOS vividos?\n'))
            if anosVividos >= 0:
                break
            print("\nPor favor, digite um número válido.")
        except:
            print("\nPor favor, digite um número válido.")

    while True:
        try:
            mesesVividos = int(input('Qual o seu total de MESES vividos?\n'))
            if mesesVividos >= 0:
                break
            print("\nPor favor, digite um número válido.")
        except:
            print("\nPor favor, digite um número válido.")

    while True:
        try:
            diasVividos = int(input('Qual o seu total de DIAS vividos?\n'))
            if diasVividos >= 0:
                break
            print("\nPor favor, digite um número válido.")
        except:
            print("\nPor favor, digite um número válido.")

    totalGeralDiasVividos = anosVividos * 365 + mesesVividos * 30 + diasVividos
    if totalGeralDiasVividos > 0:
        print("\nO seu TOTAL GERAL de DIAS vividos é de APROXIMADAMENTE", totalGeralDiasVividos)
        break
    print("\nVocê NÃO digitou VAL0RES VÁLIDOS, refaça todo o processo...")

anosVividos = 0
mesesVividos = 0
diasVividos = 0
totalGeralDiasVividos = 0