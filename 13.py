n, m = [int(i) for i in input(" ").split(" ")]
u = []
List1 = [int(i) for i in input().split()]
for _ in range(m):
    l, k = [int(i) for i in input().split()]
    u.append(min(List1[l-1:k]))
for i in u:
    print(i)
