n=int(input())
a=list(map(int,input().split()))
x=[]
for i in a:
    x.append(i*i)
x.sort()
for i in x:
    print(i,end=" ")