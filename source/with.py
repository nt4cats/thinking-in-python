lines=0

with open('/etc/dictionaries-common/words','r') as f:
    for line in f:
        lines = lines + 1

print('{} lines.'.format(lines))
