"""

3) Um supermercado tem 2 produtos em promoção, sendo que, para cada um deles, há um desconto diferente: para o primeiro
produto, deve ser dado um desconto de 8%; para o segundo, um desconto de 12%. Mostre os preços finais dos 2 produtos
após os cálculos.

"""
while True:
    try:
        primeiroProduto = float(input("Digite o valor do PRIMEIRO produto:\n"))
        if primeiroProduto > 0:
            break
        print("\nPor favor, digite um número válido.")
    except:
        print("\nPor favor, digite um número válido.")

while True:
    try:
        segundoProduto = float(input("Digite o valor do SEGUNDO produto:\n"))
        if segundoProduto > 0:
            break
        print("\nPor favor, digite um número válido.")
    except:
        print("\nPor favor, digite um número válido.")

primeiroProduto *= 0.92
segundoProduto *= 0.88
print("\nCom os DESCONTOS adicionados, os valores dos produtos agora são:")
print(f"PRIMEIRO produto = {primeiroProduto:.2f}")
print(f"SEGUNDO produto = {segundoProduto:.2f}")

primeiroProduto = 0
segundoProduto = 0
