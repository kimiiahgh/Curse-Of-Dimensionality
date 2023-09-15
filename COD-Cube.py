import numpy as np
l=[]
D=int(input("Enter the dimension D:"))
np.random.seed(1)
for i in range(0,D):
    l.append(np.random.uniform(0,1,50))
numbers=[]
for i in range(0,50):
    p=[]
    for j in range(0,D):
        p.append(l[j][i])  
    numbers.append(p)
Matrix=np.array(numbers) #including distances , each row includes a vector!
Distance=np.zeros((50,50))
for i in range(0,50):
    for j in range(0,50):
        Distance[i][j]=np.linalg.norm(Matrix[i][:] - Matrix[j][:])
        Distance[j][i]=Distance[i][j]            
MaxDist=Distance.max(axis=1)
for i in range(0,50):
    Distance[i][i]=float('inf')
MinDist=Distance.min(axis=1)
#print(Distance[0][:])
#print(MaxDist[0])
#print(MinDist[0])
avg=[0 for i in range(0,50)]
s=0
for i in range(0,50):
    avg[i]=float(float(MaxDist[i]-MinDist[i])/MinDist[i])
    s=+avg[i]
print(float(s/50))    
