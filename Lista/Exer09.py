# Construir um programa que leia nome e valor em dinheiro (reais) de uma pessoa. Calcule e retorne uma
# mensagem com o valor convertido para Dólar e calcule e retorne uma mensagem com o valor convertido para
# Euros

# to considerando
# o dolar 4,87
# o euro 5,27

valor = float(input("Informe um valor em reais: "))
dolar = valor/4.87
euro = valor/5.27
print(f"voce tem ${dolar} doloares e voce tem €{euro} em euros")