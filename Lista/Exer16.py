# 16) Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit
# para Celsius ou de Celsius para Fahrenheit, e que, a partir da resposta do usuário, faça a devida
# conversão

def main():
    ptemp = int(input("Pegunta\n"
                        "---------\n"
                        "1 - de Celsius para Fahrenheit\n"
                        "2 - de Fahrenheit para Celsius\n"
                        ": "))
    if ptemp == 1:
        CpF()
    if ptemp == 2:
        FpC()

def CpF():
    c1 = float(input("Informe a temperatura: "))
    fahr = (c1*1.8)+32
    print(f"sua temperatura em Fahrenheint é {fahr}")

def FpC():
    c2 = float(input("Informe a temperatura: "))
    cel = (c2-32)/1.8
    print(f"sua temperatura em Celsius é {cel}")
main()