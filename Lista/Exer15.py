# 15) Faça um programa que pergunte a temperatura atual para o usuário e mostre uma mensagem na
# tela dizendo se está “quente”, “frio” ou “agradável”.

temp = float(input("Qual a temperatura: "))

if (temp >= 0)and(temp <= 17):
    print("Ta frio")

elif (temp >=18)and( temp <= 20):
    print("Ta agradavel")

elif (temp >= 20)and(temp <= 30):
    print("Ta quente")

elif (temp > 30):
    print("Ta muito quente mesmo")