import math
a,b,c=map(int,input().split())
d=(a+b+c)/2
s=math.sqrt(d*((d-a)*(d-b)*(d-c)))
print(format(s,"0.2f"))