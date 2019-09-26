def buildseries(series, ite, i_count):
    checkseries = series[:-1]
    if(series[-1] not in checkseries):
        eck_sequence.append(0)
    else:
        for i, num in enumerate(reversed(checkseries)):
            if(num == series[-1]):
                eck_sequence.append(i + 1)
                break
    i_count+=1
    if( i_count < ite):
        buildseries(eck_sequence, ite, i_count)
    else:
        return

eck_sequence = []
i_count = 0
try:
    handle = open('./eck_sequence.txt', 'r')
    for line in handle:
        eck_sequence.append(int(line))
    handle.close()
except:
    eck_sequence.append(0)
    i_count = 1

ite = 500
buildseries(eck_sequence, ite, i_count)

print(len(eck_sequence))
print(eck_sequence)

handle = open('./eck_sequence.txt','w')
handle2 = open('./eck_formated.txt','w')

for i in eck_sequence:
    handle.write(str(i) + '\n')
    if( i == 0):
        handle2.write('\n' + str(i))
    else:
        handle2.write(', ' + str(i))

handle.close()
