"""

5) Solicitar o ano de nascimento de uma pessoa e o ano atual. Calcule e mostre a idade da pessoa em anos, a idade da
pessoa em meses e a idade da pessoa em dias. Obs: Para simplificar, considere arredondar o ano para 365 dias, a idade
mínima de 1 ano para ser aceito e o ano de 1900 como limite da data de nascimento.

"""
while True:
    try:
        anoNascimento = int(input("Digite o seu ANO de NASCIMENTO:\n"))
        if anoNascimento >= 1900:
            break
        print("\nPor favor, digite um número válido.")
    except:
        print("\nPor favor, digite um número válido.")

while True:
    try:
        anoAtual = int(input("Digite o ANO ATUAL:\n"))
        if anoAtual > anoNascimento:
            break
        print("\nPor favor, digite um número válido.")
    except:
        print("\nPor favor, digite um número válido.")

idade = anoAtual - anoNascimento
print("\n Você viveu um TOTAL em ANOS de APROXIMADAMENTE =", idade)
print("Você viveu um TOTAL em MESES de APROXIMADAMENTE =", idade * 12)
print(" Você viveu um TOTAL em DIAS de APROXIMADAMENTE =", idade * 365)

anoNascimento = 0
anoAtual = 0
idade = 0
