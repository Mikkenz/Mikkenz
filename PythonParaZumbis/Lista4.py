#  1. Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar
# as funções max e min.
import random
numeros = random.sample(range(100), 10)
k = 1
maior = numeros[0]
menor = numeros[0]
while k < 10:
    if numeros[k] > maior: maior = numeros[k]
    if numeros[k] < menor: menor = numeros[k]
    k += 1
print(f"Números: {numeros}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")


#  2. Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os 
# números ímpares na lista IMPAR. Imprima as três listas.
import random
numeros = random.sample(range(100), 20)
pares = []
impares = []
for x in numeros:
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)
print(f"Números: {numeros}")
print(f"Pares: {pares}")
print(f"Impares: {impares}")


#  3. Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um 
# terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos 
# intercalados dos dois outros vetores. Imprima os três vetores.
import random
numeros1 = random.sample(range(100), 10)
numeros2 = random.sample(range(100), 10)
numeros3 = []
for x, y in zip(numeros1, numeros2):
    numeros3.extend([x, y])
print(numeros1)
print(numeros2)
print(numeros3)


#  4. Seja o statement sobre diversidade: “The Python Software Foundation and the global Python 
# community welcome and encourage participation by everyone. Our community is based on 
# mutual respect, tolerance, and encouragement, and we are working to help each other live up 
# to these principles. We want our community to be more diverse: whoever you are, and 
# whatever your background, we welcome you.”. Gere uma lista de palavras deste texto com 
# split(), a seguir crie uma lista com as palavras que começam ou terminam com uma das letras 
# “python”. Imprima a lista resultante. Não se esqueça de remover antes os caracteres especiais 
# e cuidado com maiúsculas e minúsculas.
texto = """The Python Software Foundation and the global Python 
community welcome and encourage participation by everyone. Our community is based on 
mutual respect, tolerance, and encouragement, and we are working to help each other live up 
to these principles. We want our community to be more diverse: whoever you are, and 
whatever your background, we welcome you."""
texto = texto.lower()
texto = texto.replace(",", " ").replace(".", " ").replace(":", (" "))
texto = texto.split()
python = []
for p in texto:
    if p[0] in "python" or p[-1] in "python":
        python.append(p)
print(python)


#  5. Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras 
# “python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para 
# minúsculas e de remover antes os caracteres especiais
texto = """The Python Software Foundation and the global Python 
community welcome and encourage participation by everyone. Our community is based on 
mutual respect, tolerance, and encouragement, and we are working to help each other live up 
to these principles. We want our community to be more diverse: whoever you are, and 
whatever your background, we welcome you."""
texto = texto.lower()
texto = texto.replace(",", " ").replace(".", " ").replace(":", (" "))
texto = texto.split()
def é_pythonica (p):
    if len(p) <= 4:
        return False
    for c in p:
        if c in "python":
            return True
    return False


python = []
for p in texto:
    if é_pythonica(p):
        python.append(p)
print(python)
