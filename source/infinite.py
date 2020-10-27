# This is an example of a program that won't work!

def infinite_sequence():
    infinite = []
    i = 0
    while True:
        infinite.append(i)
        i = i + 1

    return infinite

for x in infinite_sequence():
    if x < 5:
        print(x)
    else:
        break
