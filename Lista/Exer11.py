# Faça um programa que receba como entrada os dados de um funcionário: nome, numero de horas
# trabalhadas, valor da hora trabalhada. Após calcule seu salário bruto. Calcule um desconto de 2% de INSS. E
# ao final mostrar seu nome e salário final calculado.

nome = str(input("Informe seu nome: "))
horas = float(input("Quantas horas trabalhadas: "))
vhoras = float(input("Valor da hora trabalhada: "))

salb = horas*vhoras
desc = salb*0.02
print(f"{desc} salario novo com desconto")
