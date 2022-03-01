a=int(input("Nombre d'iterration: "))
n=int(input ("Conjecture de Syracuse: "))
i=0
print(n)
while i < a:
    if n % 2 == 0:
      n=n//2  
    else:
        n=n*3+1
    i=i+1
    print(n)
    