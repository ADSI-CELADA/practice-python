# 1 - Crear una función max() que tome como argumento dos números y devuelva el mayor de ellos.

def numMax():
    num1 = int(input("Ingrese el primer numero "))
    num2 = int(input("Ingrese el segundo numero "))
    if num1 > num2:
        return print(num1)
    elif num2 > num1:
        return print(num2)
    else :
        return print("Ambos numeros son iguales")

numMax()





