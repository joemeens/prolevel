nun, mass = [int(i) for i in input(" ").split(" ")]
u = []
List1 = [int(i) for i in input().split()]
for _ in range(mass):
    l, k = [int(i) for i in input().split()]
    u.append(min(Lis[l-1:k]))
for i in u:
    print(i)
