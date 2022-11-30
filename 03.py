# 3 - Crear una función que calcule la longitud de una lista o una cadena dada.


# forma 1
def list():
    text = input("(forma 1) -> Ingrese su texto:\n")

    c = 0

    for i in text:
        c = c + 1

    return print('Longitud de la cadena: ' + str(c) + "\n")

list()

# forma 2

def list2():
    text2 = input("(forma 2) -> Ingrese un texto:\n") 
    return print("Longitud de la cadena: " + str(len(text2)) + "\n")

list2()

