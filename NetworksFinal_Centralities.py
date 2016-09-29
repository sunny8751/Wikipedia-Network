from networkx import *
import matplotlib.pyplot as plt
import numpy as np
from mayavi import mlab
import csv
import plotly.plotly as py


data=np.loadtxt("C:\Python34\jacqueline.txt", int)
##Idea: use a while loop with total+= <-- that should work I think for list thing
#a=data[:,0]
#b=data[:,1]
#c=data[:,2]
#d=data[:,3]
#print (a)
#print (b)
#print(c)
#a = [1,2,3,4,6]
#b = [4,5,6,3,1]
a = data[:,0]

#zipped = zip(a,b)
#zipped1=zip(a,c)
#zipped2=zip(a,d)

sunwoo = []
total =1
G=Graph()
while total != 130:
    sunwoo.extend(list(zip(a,data[:,total])))
    newSunwoo = []
    for x in sunwoo:
        if 0 not in x:
            newSunwoo.append(x)
    sunwoo = newSunwoo
    G.add_edges_from(sunwoo)
    sunwoo=[]
    total +=1

#jennifer=list(zipped1)
#akshay=list(zipped2)
#print (jennifer)
#sunwoo.extend(jennifer)
#sunwoo.extend(akshay)
#print(sunwoo)

verts =  []
for k in G.nodes():
    verts.append(k)

b = betweenness_centrality(G)
d = degree_centrality(G)
c = closeness_centrality(G)
'''
with open('murali2.csv', 'w', newline = '') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=' ', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
    for i in range(len(verts)):
        csvwriter.writerow([str(verts[i])] + [','] + [str(b[verts[i]])] + [','] + [str(d[verts[i]])]  + [','] + [str(c[verts[i]])])  
'''
betweeness = []
for i in range(len(verts)):
    betweeness.append(b[verts[i]])

plt.hist(betweeness, bins = 100)
plt.title("Network Science Depth 2 Betweenness Centrality Histogram")
plt.xlabel("Betweenness Centrality")
plt.ylabel("Frequency")
plt.show()
 

degree = []

for i in range(len(verts)):
    degree.append(d[verts[i]])

plt.hist(degree, bins = 1000)
plt.title("Network Science Depth 2 Degree Centrality Histogram")
plt.xlabel("Degree Centrality")
plt.ylabel("Frequency")
plt.show()

closeness = []

for i in range(len(verts)):
    closeness.append(c[verts[i]])

plt.hist(closeness, bins = 1000)
plt.title("Network Science Depth 2 Closeness Centrality Histogram")
plt.xlabel("Closeness Centrality")
plt.ylabel("Frequency")
plt.show()



print('Clustering Coefficient:' + str(average_clustering(G)))



'''
print("Betweenness Centrality")
b=betweenness_centrality(G)
for v in G.nodes():
    print("%0.2d %5.3f"%(v,b[v]))

print("Degree Centrality")
d=degree_centrality(G)
for v in G.nodes():
    print("%0.2d %5.3f"%(v,d[v]))

print("Closeness Centrality")
c=closeness_centrality(G)
for v in G.nodes():
    print("%0.2d %5.3f"%(v,c[v]))
'''



#print(G.nodes())
#print(G.edges())


'''
nx.draw_spring(G)
plt.show()
#nx.draw_shell(G)
#plt.show()
#nx.draw_spectral(G)
#plt.show()
#nx.draw(G)
#plt.show()
nx.draw_circular(G)
plt.show()
'''

