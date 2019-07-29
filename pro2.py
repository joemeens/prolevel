string1,string2=input(" ").split(" ")
cost_differnce=abs(len(string1)-len(string2))
for i in range(len(string1)):
    if len(string2)==1 and string2[i] in string1:
        break
    if string1[i] != string2[i]:
        cost_differnce+=1 
print(cost_differnce)
