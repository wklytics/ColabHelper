# if  you run start colabHelper from scratch, 
# >>> do below
#!git clone https://github.com/wklytics/ColabHelper.git
#from ColabHelper.utility.Interactive import *
# << end do

#here you are WITHIN the colabHelper folder, so the import is different
from utility.Interactive import *


# define a normal function with plot;

# example: 
import numpy as np
import matplotlib.pyplot as plt
def test_plot(phase,ampl,factor, fix1,fix2):
  x=np.linspace(0,10,100);
  y=np.sin(factor*x + factor* x*x + phase) * ampl + fix1 * x;
  y2= np.cos(factor*x + x*x + phase) * ampl + fix2 * x;
  plt.plot(x,y)
  plt.plot(x,y2)
  plt.show()
  plt.close()

# add the wrapper
interact(test_plot,phase=[0.5,5,0.5], ampl=[1.0,5.0,0.5],factor=[1.0,10.0,0.5], 
         fix1=0.1, fix2=0.2);
