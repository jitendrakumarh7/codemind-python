import math
a,b,c=map(int,input().split())
amt=a*(pow(1+(b/100),c))
print(format(amt,"0.2f"))