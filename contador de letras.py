import string
alphabet = (string.ascii_lowercase)
aLPHABET = (string.ascii_uppercase)

def contadorLetras(y):
    for letters in alphabet:
        print(f"Quantidade de \"{letters}\" na frase: {y.count(letters)} letra(s)")

contadorLetras(input("Digite sua Frase: "))
