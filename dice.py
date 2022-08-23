def fun(a,b):
    c={0:1}
    for time in range(1,b+1):
        c[time]=0
        for x in a:
            c[time]+=c.get(time-x,0)
    return c[time]
d=int(input())
for _ in range(d):
    e,f= map(int,input().split())
    a=[]
    for i in range(1,f+1):
        a.append(i)
    print(fun(a,e))
