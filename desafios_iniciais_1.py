#Calcular a média de uma lista de números: 
#Crie um programa que receba uma lista de números e retorne a média dos valores presentes na lista.
menu = """

[S] Digite números para que a média seja calculada
[N] Não deseja mais números

"""
opcao = str.upper(input (menu))
i = 0
grupo = []

while opcao == "S":

    x = input("Digite um número: ")
    grupo.append(int(x))
    i = i + int(x)
    quantidade = len(grupo)        
    media = i / quantidade
    opcao = str.upper(input (menu))

print(f"Para o grupo de números {grupo} a média é de: {media}")
