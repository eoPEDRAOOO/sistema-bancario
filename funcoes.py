def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b


def mostrar_função(a, b, função):
    resultado = função(a, b)
    print(f"o resultado da operação é {a} + {b} = {resultado}")
    
    
mostrar_função(9, 9, somar)
mostrar_função(9, 3, subtrair)