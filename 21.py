import statistics as st
count=int(input(" "))
array=list(map(int,input().split()))
result=False
for i in range(1,count):
    list1=array[:i]
    list2=array[i:]
    if st.mean(list1)==st.mean(list2):
        result=True
if result==True:
    print("yes")
else:
    print("no")
