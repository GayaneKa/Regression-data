import numpy as np
import xarray as xr
import pandas as pd
#from sklearn.linear_model import LinearRegression
from sklearn import svm
from matplotlib import pyplot as plt 

class main:
  def __init__(myobject, Mean, Sigm, lst):
    myobject.Mean = Mean
    myobject.Sigm = Sigm
    myobject.NMean = np.mean(lst)
    myobject.NSigm = np.std(lst)
    myobject.Arr = lst
  def myfunc(myobject):
    gn = np.random.normal(myobject.Mean, myobject.Sigm, (100,100))
    return(gn)
  def myfunc2(myobject):
    gn = np.random.normal(myobject.Mean, myobject.Sigm,100)
    return(gn)
  def newfunc(myobject):
    print('Mean =', myobject.NMean,'Sigma =',myobject.NSigm)
  def plotting(myobject):
    #plt.hist(myobject.Arr, bins='auto')
    #plt.hist(myobject.Arr)
    plt.hist(myobject.Arr)
    #plt.title("histogram") 
    plt.show()
    
    
def Samples(mean):
    mu = mean
    sigma = 1
    A = main(0,1,[0,0]).myfunc()
    B = main(mu,sigma,[0,0]).myfunc2()
    F = A.copy()
    if mu == 0 :
        print
        #main(mu,sigma,A).newfunc()
        #main(mu,sigma,A).plotting()
    else:
        for j in range(0, 100,mean):
            #print(j)
            if j%mean == 0:
                #print(j)
                F[j-1] = B
        E = F.copy()
        print(F)
        #main(mu,sigma,E).newfunc()
        #main(mu,sigma,E).plotting()

        
Samples(0)