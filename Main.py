import pandas as pd
import numpy as np
import random
import time
import SamplePath

hrsOfSimulation = 1
N=(2,4,5,8,10)
lim = 100
grid = []
for n in N:
    a = time.time()
    ans=0
    for i in range(lim):
        zz=SamplePath.SamplePath(n,hrsOfSimulation*10000)
        ans +=zz
        print(i,zz,ans/(i+1),time.time()-a)
    b=time.time()
    #print(ans/lim,b-a)
    theoreticalAns = (2/(n+1))*(hrsOfSimulation*10000-1000/n)*n
    n_ans = [n,ans/lim,lim,b-a,theoreticalAns]
    print(pd.DataFrame(n_ans,index=["n","SortedItems_Sim","SamplePaths","timeTaken","SortedItems_Th"]).T)
    grid.append(n_ans)

grid = pd.DataFrame(grid)
grid.columns=["n","SortedItems_Sim","SamplePaths","timeTaken","SortedItems_Th"]
print(grid)
name = str(hrsOfSimulation)+"_hr_Sim.csv"
grid.to_csv(name)