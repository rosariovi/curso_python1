print("ingresa un numero")
a=int(input())
print("ingresa un segundo numero")
b=int(input())
print("ingresa un tercer ")
c=int(input())
if a>b and a>c:
    print("el numero mayor es  ", a)
elif b>a and b>c:
    print("el numero mayor es el segundo numero =  ", b)
else:
    print("el numero mayor es el tercer numero =  ", c)