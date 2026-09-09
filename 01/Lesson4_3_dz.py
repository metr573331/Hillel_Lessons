import random

a = [random.randint(1, 50) for _ in range(random.randint(5, 15))]
aa = [a[0], a[2], a[-2]]

print(a)
print(aa)
