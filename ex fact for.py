n=int(input('enter a terms:'))
x=int(input('enter a x value:'))
e=1
k=1
for i in range(1,n+1):
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    e=e+((-1)**k)*((x**i)/fact)
    k=k+1
print(e)
