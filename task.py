import math
def f(x):
  return x-1/(3+math.sin(3.6*x))
a=0
b=1
eps=0.00001
fa=f(a)
for i in range(100): 
  x=a-(f(a)*(b-a))/(f(b)-f(a))
  fx=f(x) #высота графика в центре
  if abs(f(x))<eps or (b-a)<eps: #есть ли на этом этапе корень
    print(x)
    break
  if f(a)*f(x)<0: #корня нет, уменьшаем диапазон
    b=x
  else:
    a=x
    fa=fx
