#task1.2
import numpy as np
l=[]
D=int(input("Enter the dimension D:"))
np.random.seed(1)
for i in range(0,D):
    l.append(np.random.uniform(0,100,10))
numbers=[]
for i in range(0,10):
    p=[]
    for j in range(0,D):
        p.append(l[j][i])  
    numbers.append(p)
Matrix=np.array(numbers)
from sklearn.neighbors import NearestNeighbors
neigh = NearestNeighbors(n_neighbors=7) #ba khode har noqte
neigh.fit(Matrix)
dist=[]
for k in Matrix:
    dist.append(neigh.kneighbors([k])) #dist 6 nearest
avg=[]
for i in range(0,10):
    c=0
    for j in range(0,6):
        #dist[i][0][0][j]
        c=c+float(dist[i][0][0][j])
    c=float(c/6)    
    avg.append(c)
print(avg) 
