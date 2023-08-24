#8) Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua área e a
# quantidade da tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².

larg = float(input("Digite a largura da parede em metros: "))
alt = float(input("Digite a altura da parede em metros: "))

area = larg*alt

litros = area/2
print(f"voce precisa de {litros} litros de tinta")

