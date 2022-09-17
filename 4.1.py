import math 
def func (x):
    y=(math.log(x, math.e) - math.log10(x) + math.log(4*x,2))/(math.fabs(math.cos(x))+0.4) + 0.12*(3*x+3)**(1/5)
    return y 
print(func(float(input("x="))))    