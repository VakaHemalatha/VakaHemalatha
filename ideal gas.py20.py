p=int(input('enter the pressure:'))
v=int(input('enter the volume:'))
t=float(input('enter the temp:'))
r=float(input('enter the gas constant:'))
n=(p*v)/(r*(t+273.15))
print('the number of mole is',n)
