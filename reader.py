texto = "Texto teste"
alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# dicionário com as letras do alfbeto como chave e 0 como valor
dict = {letra: 0 for letra in alph}

# compara as letras do alfabeto com as do texto e salva no dicionário somando a quantidade de cada uma
for letra in texto.lower():
    for let in alph:
        if letra == let:
            dict[let] = dict[let]+1

           

