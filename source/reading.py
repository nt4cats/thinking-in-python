words = open('/etc/dictionaries-common/words','r')

lines = 0

try:
    for line in words:
        lines = lines + 1
finally:
    try:
        words.close()
    except:
        # not much we can do if this fails
        pass

print('{} lines.'.format(lines))
