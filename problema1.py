
a = int(input("numero 1: "))
b = int(input("numero 2: "))

def Mult(a,b):
    c=0
    if a<0 or b<=0:
        return  # no retornas nada. Supongo que quieres que la funcion retorne algún valor.

    b=b-1
    c=c+a
    a=c+a

    Mult(a,b)  # ¿el resultado de esta función dónde se almacena?
    print c

Mult(a,b)
