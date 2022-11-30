# 5 - Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

nums = [1, 2, 3, 4, 5]


def sum():
    suma = 0
    for i in nums:
        suma = suma + i

    print("El resultado de la suma es de: " + str(suma))


sum()


def mult():
    mult = 1
    for i in nums:
        mult = mult * i

    print("El resultado de la multiplicacion es de: " + str(mult))


mult()
