import math
def f(x):
    return x**2 + math.log(x)

def bisection(a, b, tol):
   
    if f(a) * f(b) >= 0:
        print("O método da bissecção não pode ser aplicado.")
        return None
    else:
        c = a
        while (b-a) >= tol:
            c = round((a+b)/2,2)
            if f(c) == 0.0:
                break
            if f(c)*f(a) < 0:
                b = round(c,2)
            else:
                a = round(c,2)
        return c

a = 0.5
b = 1
tol = 0.01

root = bisection(a, b, tol)
print("A raiz é: ",root )
