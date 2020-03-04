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
    gn1 = pd.DataFrame(np.random.normal(myobject.Mean, myobject.Sigm, (100,100)))
    return(gn1)
  def myfunc2(myobject):
    gn2 = np.random.normal(myobject.Mean, myobject.Sigm,100)
    return(gn2)
  def newfunc(myobject):
    print('Mean =', myobject.NMean,'Sigma =',myobject.NSigm)
  def plotting(myobject):
    plt.hist(myobject.Arr) 
    plt.show()
    
    
def Samples(mean):
    mu = mean
    sigma = 1
    A = main(0,1,[0,0]).myfunc()
    B = main(mu,sigma,[0,0]).myfunc2()
    if mean == 0:
        F = A.copy()
    else:
        A[mean] = B
        F = A.copy()
    return(F)
    '''E = F.copy()
    main(mu,sigma,E).newfunc()
    main(mu,sigma,E).plotting()'''
    
       
print(Samples(0))