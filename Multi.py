print("Multiplication Egyptienne :")

a=int(input("Premier nombre: "))
b=int(input ("Deuxieme nombre: "))

i = 0
while a != 0:
    if (a % 2) == 1:
        i = i+b
    b = b*2
    a = a//2
print(i)