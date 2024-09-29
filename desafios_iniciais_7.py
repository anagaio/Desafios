#Encontrar o maior elemento em uma lista: Escreva um programa que encontre o maior elemento em uma lista de números.

x = []
número = input("Digite um número: ")
x.append(float(número))
mais_numero = str.upper(input("Quer digitar mais números? S/N\n"))

while mais_numero == "S":

    número = input("Digite um número: ")
    x.append(float(número))
    mais_numero = str.upper(input("Quer digitar mais números? S/N\n"))

x.sort()
print(f"Entre os números {x} o maior número é {x[-1]}")
             