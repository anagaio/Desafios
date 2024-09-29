#Contar a quantidade de vogais em uma palavra: Desenvolva uma função que receba uma palavra como entrada e retorne a quantidade de vogais presentes na palavra.
palavra = str.lower(input("Digite uma palavra: "))
vogais = ["a", "e", "i", "o", "u"]
quantidade = {}

for i in vogais:
    if i in palavra:
        quantidade[i] = palavra.count(i)

print(quantidade)
