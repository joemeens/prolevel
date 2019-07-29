test=int(input(" "))
array=list(map(int,input().split()))
c=[]
count=1
for i in array:
  if i not in c:
    c.append(i)
for i in range(0,len(c)-1):
  if c[i]<c[i+1]:
    count+=1
print(count)
