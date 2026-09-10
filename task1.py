import math
def f(x):
  return x-1/(3+math.sin(3.6*x))
a=0
b=1
eps=0.00001
while (b-a)/2>eps:
  c=(a+b)/2
  if f(a)*f(c)<0: 
    b=c #знаки разные, значит корень в левой части
  else:
    a=c #иначе корень в правой части
answer = (a+b)/2
print(answer)
