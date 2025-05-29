# abrindo o arquivo com o texto
with open('arquivo.txt', 'r', encoding="utf-8") as arquivo:
    texto = arquivo.read()

alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# dicionário com as letras do alfbeto como chave e 0 como valor
dict = {letra: 0 for letra in alph}

# compara as letras do alfabeto com as do texto e salva no dicionário somando a quantidade de cada uma
for letra in texto.lower():
    if letra in alph:
        dict[letra] = dict[letra]+1

# calculando total de caracteres presentes no alfabeto
total = 0
for l in texto.lower():
    if l in alph:
        total+=1

# calculando a porcentagem de cada letra e salvando em um dicionário
porc = {letra: 0 for letra in alph}
for letra, quant in dict.items():
    porc[letra] = quant*100/total

# Saída
print("QUANTIDADE DE CADA LETRA")
print('='*50)
for letra, quant in dict.items():
    print(f"{letra.upper()}: {quant}")
print('='*50)

print("PORCENTAGEM DE CADA LETRA")
for letra, quant in porc.items():
    print(f"{letra.upper()}: {quant:.1f}%")