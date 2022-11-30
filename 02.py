# 2 - Crear una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

def numMax():
    n1 = int(input("Ingrese el primer numero "))
    n2 = int(input("Ingrese el segundo numero "))
    n3 = int(input("Ingrese el tercer numero "))
    if n1 > n2 and n1 > n3:
        return print(n1)
    elif n2 > n3 and n2 > n1:
        return print(n2)
    elif n3 > n1 and n3 > n2:
        return print(n3)
    else:
        return print("Los tres numeros son iguales")

numMax()