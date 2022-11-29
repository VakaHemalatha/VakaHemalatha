a=[1,2,3,4,5,6,7,8,9,10]
print(a)
n=int(input('pick any one element from the above list:'))
i=a.index(n)
j=len(a)-1
b=list()
if a[i]==a[j]:
    print(a)
else:
    for k in range(1,j-1+1):
        for p i range(0,j+1):
            if p==0:
                b.append(a[j])
            else:
                b.insert(p,a[p-1])
        a=b
        b=list()
print(a)
