kin,mis=map(int,input(" ").split(" "))
mk=list(map(int,input().split()))
list1=[]
for i in range(0,mis):
     a,b=map(int,input().split())
     list1.append([a,b])
for i in range(mis):
     lower=list1[i][0]
     upper=list1[i][1]
     x=sum(mk[lower-1:upper])
     print(x)
