#  1) Faça um programa que peça dois números inteiros e imprima a soma desses dois números
a = int (input ("Primeiro número: "))
b = int (input ("Segundo número: "))
    print (a + b)


#  2) Escreva um programa que leia um valor em metros e o exiba convertido em milímetros
m = int(input("Metragem: "))
print ('Conversão em milímetros: '); print(m * 1000)


#  3) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule
# o total em segundos.
d = int(input("Dia: "))
h = int(input("Horas: "))
m = int(input("Minutos: "))
s = int(input("Segundos: "))
c = d * 24 * 60 * 60 + h * 60 * 60 + m * 60 + s
print()
print ("Tudo em segundos: "); print(c)


#  4) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
# porcentagem do aumento. Exiba o valor do aumento e do novo salário.
s = float(input("Qual o salário?: "))
a = int(input("Quantos % irá aumentar?: "))
ar = s * a / 100
ra = s + ar
print("Irá aumentar: "); print(ar)
print("Novo Salário: "); print(ra)


#  5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o
# preço a pagar.
p = float(input("Preço: "))
d = float(input("Desconto: %"))
por = p * d / 100
des = p - por
print(f"Desconto de: ${por:.2f}")
print(f"Preço final: ${des:.2f}")


#  6) Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média
# esperada para a viagem.
d = float(input("Qual a distância: "))
v = int(input("Qual será a velocidade média: "))
t = d / v
print(f"tempo estimado de viagem em horas:{t:.1f}")


#  7) Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32
C = int(input("Temperatura em °C: "))
F = 9*C/5 + 32
print("Fahrenheit: "); print(F)


#  8) Faça agora o contrário, de Fahrenheit para Celsius.
F = int(input("Temperatura em °F: "))
C = (F - 32) * 5 / 9
print("Celsius: "); print(C)


#  9) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
# usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
k = float(input("Km Rodados: "))
d = int(input("Quantos dias o carro está alugado: "))
p = 60 * d + 0.15 * k
print("Preço final em R$: ");print(p)


#  10) Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
# quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
# perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
# total de dias.
anos = int(input("Anos: "))
cigarros = int(input("Cigarros: "))
total = anos * 365 * cigarros
vida_perdida = total / 144
print(f"Você perdeu {vida_perdida: .2f} dias")


#  11) Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado
# a um milhão
n = int(len(str((2**1000000))))
print (n)
