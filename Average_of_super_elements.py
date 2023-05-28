n=int(input())
l=list(map(int,input().split()))
mx=max(l)
s=0
c=0
ct=0
case=0
for i in range(1,mx+1):
    c=0
    for j in l:
        if i==j:
            c=c+1
    if c==i:
        s=s+i
        case=1
        ct=ct+1
if case==1:
    print(format(s/ct,"0.2f"))
else:
    print("-1")
        