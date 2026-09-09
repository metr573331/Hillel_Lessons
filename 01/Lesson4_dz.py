a = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

counter = 0

while 0 in a:
    a.remove(0)
    counter += 1

while counter > 0:
    a.append(0)
    counter -= 1

print(a)
