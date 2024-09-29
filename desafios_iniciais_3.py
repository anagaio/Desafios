#Converter temperatura de Celsius para Fahrenheit: Escreva um programa que converta uma temperatura em graus Celsius para Fahrenheit.
temperatura = str.upper(input("Indique se a temperatura está em Celsius (C) ou Fahrenheit (F): "))
graus = float(input("Digite a temperatura: "))

if temperatura == "F":

    celcius = (graus-32) / 1.8
    print(f"A temperatura {graus} {temperatura} é equivalente a {celcius :.2f} C")

else:

    farenheit = (graus*1.8) + 32
    print(f"A temperatura {graus} {temperatura} é equivalente a {farenheit :.2f} F")
