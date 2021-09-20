#  1. Dizemos que um número natural é triangular se ele é produto de três números naturais 
# consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, 
# verificar se n é triangular.
t = int(input("Digite o valor de n: "))
n = 1
while n * (n+1) * (n+2) < t:
        n = n + 1
if n * (n+1) * (n+2) == t:
    print(f"{t} é o produto de {n} * {n + 1} * {n + 2}")
else:
    print(f"{t} não é triangular")


#  2. Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu 
# algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado desprezando 
# os centavos. Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que 
# nenhuma delas esteja em falta no caixa.
valorDaConta = int(input("Valor total da conta: "))
valorDoPagamento = int(input("Pagamento efetuado de: "))
caixa = [50, 20, 10, 5, 2, 1]
troco = valorDoPagamento - valorDaConta
for notas in caixa:
    if troco >= notas:
        quantidade = troco / notas
        r = troco - (notas * int(quantidade))
        print(int(quantidade),"notas de R$",notas)
        troco = r


#  3. Verifique se um inteiro positivo n é primo.
numero = int(input("Digite um número inteiro: "))
contador = 0
i = 0
while i <= numero or contador < 2:
    i = i + 1
    x = numero % i
    if x == 0:
        contador += 1
if contador <= 2:
    print("primo")
else:
    print("não primo")


#  4. Dado um número inteiro positivo, determine a sua decomposição em fatores primos 
# calculando também a multiplicidade de cada fator.
n = int(input("Número: "))
for k in range(2, n):
    while n % k == 0:
        print(k)
        n = n / k


#  5. Faça um programa que peça um inteiro positivo e o mostre invertido. Ex.: 1234 gera 4321
sequencia = int(input("Sequencia: "))
sequencia = str(sequencia)
sequencia = sequencia[::-1]
print(sequencia)
