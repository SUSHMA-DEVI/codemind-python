a=list(map(str,input().split()))
m=0
for i in range(0,len(a)):
    if len(a[i])>m:
        m=len(a[i])
print(m)
    