
f = open ('network3.txt', 'r')
list1 = []
length = 0
for line in f.readlines():
    list1.append(line)
    if (line.count('\t')) > length:
        length = line.count('\t')
f.close()

print ('length:', length)

fw = open('output.txt', 'w')
for i in list1:
    n = length-line.count('\t')
    #print len(i.split())
    i=i+'0\t'*n+'\n\n'
    fw.write(i.strip('\n'))
fw.close()

'''
f = open ('output.txt', 'r')
for line in f.readlines():
    print(len(line.split('\t')))
f.close()
'''

f = open('output.txt','r')
for line in f.readlines():
    print(len(line.split()))

