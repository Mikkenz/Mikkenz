#  1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
# seja inválido e continue pedindo até que o usuário informe um valor válido.
nota = int(input("Entre um número de 0 a 10: "))
while nota > 10 or nota < 0:
    print("número inválido")
    nota = int(input("tente novamente: "))
print(f"O número é: {nota}")


#  2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
# nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
usuario = input("Entre com um nome de usuário: ")
senha = input("Entre com a senha: ")
while usuario == senha:
    print("A senha e o usuário devem ser diferentes, reentre")
    usuario = input("Entre com um nome de usuário: ")
    senha = input("Entre com a senha: ")
print("Bem vindo")


#  3. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa
# anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de
# crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
# necessários para que a população do país A ultrapasse ou iguale a população do país B,
# mantidas as taxas de crescimento
paisA = 80000
paisB = 200000
taxaA = 3/100
taxaB = 1.5/100
ano = 0
while paisA < paisB:
    paisA += taxaA * paisA
    paisB += taxaB * paisB
    ano += 1
print(f"serão necessários {ano} para que o país A passe o país B")


#  4. A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de 
# formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a 
# soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número 
# de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.
n = int(input("Que termo deseja encontrar: "))
ultimo=1
penultimo=1
if (n==1) or (n==2):
    print("1")
else:
    count=3
    while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(termo)


#  5. Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando 
# o algoritmo de Euclides.
n1 = int(input("primeiro número: "))
n2 = int(input("segundo número: "))
mdc = 1
divisor = 2
while divisor <= n1 or divisor <= n2:
    if n1>1 and n2>1 and n1 % divisor == 0 and n2 % divisor ==0:
        print(int(n1),int(n2),divisor)
        n1 = n1/divisor
        n2 = n2/divisor
        mdc = mdc * divisor
    elif n1>1 and n2>1 and n1 % divisor == 0 or n2 % divisor ==0:
        while divisor <= n1 or divisor <= n2:
            if n1 % divisor == 0:
                print(int(n1),int(n2),divisor)
                n1 = n1/divisor
                mdc = mdc * divisor
            elif n2 % divisor == 0:
                print(int(n1),int(n2),divisor)
                n2 = n2/divisor
                mdc = mdc * divisor
            break
    else:
        divisor += 1
print('mdc: ',mdc)
