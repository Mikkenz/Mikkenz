#  1. Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser
# um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
a = int(input("Primeiro valor para o triangulo: "))
b = int(input("Segundo valor para o triangulo: "))
c = int(input("Terceiro valor para o triangulo: "))
if  a + b > c and a + c > b and b + c > a:
    print("Pode ser um triangulo")
    if a == b == c:
        print("É um triangulo equilátero!")
    elif a == b != c or a == c != b or b == c != a:
        print("É um triangulo isósceles!")
    else:
        print("É um triangulo escaleno!")
else :
    print("Não pode ser um triangulo!")


#  2. Determine se um ano é bissexto. Verifique no Google como fazer isso...
ano = int(input('Ano: '))
if ano % 4==0 and ano % 100 !=0 or ano % 400 == 0:
    print('Bissexto')
else:
    print('Não é bissexto')


#  3. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de 
# seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do 
# estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você 
# faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na 
# variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais 
# variáveis com o conteúdo ZERO.
print("LIMITE DE 50Kg")
peso = float(input())
if peso > 50.0:
    excesso = peso - 50
    multa = 4 * excesso
    print(f"O excesso de peso é {excesso}Kg")
    print(f"Sua multa é de R${multa: .2f}")
else:
    print("ZERO")
    print("ZERO")


#  4. Faça um Programa que leia três números e mostre o maior deles.
a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    print(f"O maior número é: {a}")
if b > a and b > c:
    print(f"O maior número é: {b}")
if c > a and c > b:
    print(f"O maior número é: {c}")


#  5. Faça um Programa que leia três números e mostre o maior e o menor deles.
a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    print(f"O maior número é: {a}")
if b > a and b > c:
    print(f"O maior número é: {b}")
if c > a and c > b:
    print(f"O maior número é: {c}")
if a < b and a < c:
    print(f"O menor número é: {a}")
if b < a and b < c:
    print(f"O maior número é: {b}")
if c < a and c < b:
    print(f"O menor número é: {c}")


#  6. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule 
# e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS, 
# quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os 
# descontos e o salário líquido, conforme a tabela abaixo:
# a. + Salário Bruto : R$
# b. - IR (11%) : R$
# c. - INSS (8%) : R$
# d. - Sindicato ( 5%) : R$
# e. = Salário Liquido : R$
print("Quanto você ganha por hora?")
ganho = int(input())
print("Horas trabalhadas no mês: ")
horas = float(input())

salarioBruto = ganho * horas
impostoRenda = salarioBruto * 11 / 100
inss = salarioBruto * 8 / 100
sindicato = salarioBruto * 5 /100
salarioLiquido = salarioBruto - impostoRenda - inss - sindicato

print(f"Salário Bruto R${salarioBruto: .2f}")
print(f"Imposto de Renda R${impostoRenda: .2f}")
print(f"INSS R${inss: .2f}")
print(f"Sindicato R${sindicato: .2f}")
print(f"Slário Líquido R${salarioLiquido: .2f}")


#  7. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a 
# ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
# em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem 
# compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas
metros = int(input("metros: "))
if metros % 54 == 0:
    latas = metros / 54
else:
    latas = int(metros / 54) + 1

preco = latas * 80
print(f"serão necessárias {latas} latas")
print(f"Valor total de R${preco:.2f}")
