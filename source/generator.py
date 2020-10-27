def infinite_sequence():
    i = 0
    while True:
        yield i
        i = i + 1

for x in infinite_sequence():
    if x < 5:
        print(x)
    else:
        break
