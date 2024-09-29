#Verificar se uma palavra é um palíndromo: 
# Implemente um programa que verifique se uma palavra é um palíndromo, ou seja, se pode ser lida da mesma forma tanto da esquerda
# para a direita quanto da direita para a esquerda.

palavra = str(input("Digite uma palavra: "))
palavra_contr = palavra[::-1]

if palavra == palavra_contr:

    print("Essa palavra é um palíndromo")

else:

    print("Essa palavra não é um palíndromo")
