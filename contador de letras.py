import string
alphabet = (string.ascii_lowercase)
aLPHABET = (string.ascii_uppercase)

def contadorLetras(y):
    for letters in alphabet:
        if y.count(letters) > 0:
            print(f"Quantidade de \"{letters}\" na frase: {y.count(letters)} letra(s)")
    print()
    print("ATENÇÃO!!!")
    print("Esse programa NÃO contabiliza letras com acentos")
    print("Nem números")
    print("Ex.: 'é', 'ç', '12', entre outros...")
contadorLetras(input("Digite sua Frase: "))
