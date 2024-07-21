"""

1) Um funcionário recebe um salário mensal, que deve ter 15% de desconto e um acréscimo de 100 reais. Exibir o salário
final após os cálculos.

"""
while True:
    try:
        salarioFuncionario = float(input('Qual o valor do seu SALÁRIO?\n'))
        if salarioFuncionario > 0:
            break
        print("\nPor favor, digite um número válido.")
    except:
        print("\nPor favor, digite um número válido.")

salarioFuncionario *= 0.85
salarioFuncionario += 100
print(f"O valor do seu NOVO SALÁRIO é de {salarioFuncionario:.2f}")

salarioFuncionario = 0