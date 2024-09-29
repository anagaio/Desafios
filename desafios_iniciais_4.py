#Calcular o fatorial de um número: Crie uma função que calcule o fatorial de um número dado como entrada.
numero = int(input("Digite um número: "))
i = 1

while numero >= 2:

    fatorial = numero * (numero - 1)
    numero = numero - 2
    i = i * fatorial
    
print(f"O fatorial é {i}")
