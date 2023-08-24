# 7) Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto e com 15%
# de aumento.

produto = float(input("Digite o valor do produto: "))
desc1 = produto*0.05
print(f"R${desc1} com desconto 5% de desconto")
desc2 = produto*0.15
print(f"R${desc2} com desconto de 15% de desconto")