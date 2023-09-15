#task 1.4
import math
def v_NBall(D,R):
    return float((pow((math.pi),(D/2)))/math.gamma((float(D/2))+1)) * (pow(R,D))
def v_NCube(D,S):
    return pow(S,D)
D=[1,2,3,4,5,6,10,20,50,100]

for i in D:
    print("In",i,"Dimension :")
    print("voloum of ",i,"sphere is:",v_NBall(i,5))
    print("voloum of ",i,"cube is:",v_NCube(i,10))
    print(v_NBall(i,5)/v_NCube(i,10))
    print("")
