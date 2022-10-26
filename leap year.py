n=int(input('enter a year:'))
if n%400==0 and n%100==0:
    print('it is leap year')
elif n%4==0 and n%100!=0:
    print('it is leap year')
else:
    print('it is not leap year')
