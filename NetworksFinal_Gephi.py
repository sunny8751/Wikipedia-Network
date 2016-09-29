from networkx import *
import matplotlib.pyplot as plt
import numpy as np
from mayavi import mlab

data=np.loadtxt("C:\Python34\jacqueline.txt", int)
sunwoo =[]
a = data[:,0]
total =0
while total != 131:
    sunwoo.extend(list(zip(a,data[:,total])))
    total +=1
newSunwoo = []

for x in sunwoo:
    if 0 not in x:
        newSunwoo.append(x)
sunwoo = newSunwoo
'''
f = open('akshay.txt', 'w')
f.write('graph' +  '\n' +'[' + '\n')
for line in a:
    f.write('  node' + '\n' + '  [' + '\n' + '    id ' + str(line)+'\n' + '    label ' +'"'+ str(line)+'"' + '\n' '  ]' + '\n')
for line in sunwoo:
    f.write('  edge' + '\n' + '  [' + '\n' + '    source ' + str(line[0]) + '\n' + '    target ' + str(line[1]) + '\n' + '    value 1' + '\n' + '  ]' + '\n')
f.close()
'''

f = open('akshay.dl', 'w')
f.write('DL n=1539' + '\n' + 'format = edgelist1' + '\n' + 'data:' + '\n')
for line in sunwoo:
    f.write(str(line[0]) + ' ' + str(line[1]) + '\n')
f.close()



