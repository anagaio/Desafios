#Verificar se um número é primo: Implemente um programa que verifique se um número é primo, ou seja, se é divisível apenas por 1 e por ele mesmo.
x = 1
numero = int(input("Digite um número: "))
numero_2 = numero + 1
lista = []

while x <= numero:
    calc = numero % x
    lista.append(float(calc))
    x += 1

if lista[0] == 0 and lista[-1] == 0 and lista[1] != 0 and lista[-2] != 0:

    print("Esse número é primo")

else:

    print("Esse número não é primo")
