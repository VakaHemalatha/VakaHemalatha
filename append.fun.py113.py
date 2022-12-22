n=str(input(' entera first string:'))
a=list()
while n!='':
    if n not in a:
        a.append(n)
    n=str(input('enter next string:'))
for i in a:
    print(i)
