import math 
x1=float(input("x="))
y1=float(input("y="))
z1=float(input("z="))
M= math.fabs(math.sin(x1)**2-y1*math.e**(2*z1))+math.sqrt(math.fabs(z1)+2)-((x1+y1)/math.log2(math.fabs(z1)))
print (M)