# 4 - Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def vocales():
    text = input("Ingrese una vocal\n")
    if text == 'a' or text == 'e' or text == 'i' or text == 'u':
        return print(True)
    else:
        return print(False)


vocales()
