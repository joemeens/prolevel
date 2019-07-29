count=int(input(" "))
array=list(map(int,input().split()))
array.sort(reverse=True)
#print(arr)
sum=0
sum1=0
result=[]
for i in range(0,count,2):
    sum=sum+array[i]
for j in range(1,count,2):
    sum1=sum1+array[j]
result.append([sum,sum1])
#print(res)
for i in result:
    print(i[0] if i[0]>i[1] else i[1])
