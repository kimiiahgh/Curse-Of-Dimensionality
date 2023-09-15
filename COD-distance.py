#task1.1
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import matplotlib
def distr(points,D):
    lim=[((i*20)+20) for i in range(0,5)] #lim[0]=20 : 0<=x<20
    parts=[]
    if D==1:
        parts=lim
    elif D==2:
        for i in range(0,5):
            for j in range(0,5):
                parts.append([lim[i],lim[j]])
    elif D==3:
        for i in range(0,5):
            for j in range(0,5): 
                for k in range(0,5):
                    parts.append([lim[i],lim[j],lim[k]])              
    distrb=[0 for i in range(0,len(parts))]     
    for j in range(0,len(points)):
        for i in range(0,len(parts)):
            if D==1:
                if points[j]<=parts[i]:
                    distrb[i]+=1
                    break
            else:    
                if points[j][0]<=parts[i][0] and points[j][1]<=parts[i][1]:
                    distrb[i]+=1
                    break
    return distrb,parts          
################                
        
l=[]
D=int(input("Enter the dimension D:"))
np.random.seed(1)
for i in range(0,D):
    l.append(np.random.uniform(0,100,50))
numbers=[]
for i in range(0,50):
    p=[]
    for j in range(0,D):
        p.append(l[j][i])  
    numbers.append(p)
Matrix=np.array(numbers) #including distances , each row includes a vector!
if D==1:
    x=l[0]
    plt.title('Distribution of 50 numbers')
    plt.hist(l[0], bins=5)
    plt.show()
    plt.title('The plot of these numbers in 1Dimension')
    y=[0 for i in range(0,50)]
    plt.scatter(x,y, c='r')
    plt.show()
    distribution=distr(Matrix,D)
elif D==2:
    plt.scatter(l[0], l[1])
    plt.show()
    distribution=distr(Matrix,D)
elif D==3:
    label=[0,1,2]
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter3D(l[0], l[1], l[2]);  
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    distribution=distr(Matrix,D)
print("Different Parts")    
print(distribution[1])
print("")
print("Distribution of each part")  
print(distribution[0]) 
