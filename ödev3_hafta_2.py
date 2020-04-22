#CAN KURTTEKİN
#170401015

import sympy as sym                 
from sympy import Symbol
from sympy import pprint
import matplotlib.pyplot as plt

#x ve lambda için sembollerinin tanımlanması:
x=Symbol('x')
l=Symbol('lambda')
exponential = (l*(sym.exp(-l*x)))   #exp() fonk ile e üssü alınır
pprint(exponential)
sym.plot(exponential.subs({l:0.5}),(x,0,10),title="Exponential Disturbiton")    #verilen değerler: l=0.5  x=(0,10)
plt.show()
x_val=[]
y_val=[]
#döngü içerisinde, x için bulunan y değerleri listeye atılıyor.
for i in range(11):
    y=exponential.subs({x:i, l:0.5}).evalf()
    x_val.append(i)
    y_val.append(y)
plt.plot(x_val, y_val)
