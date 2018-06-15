#Import
import numpy as np
import sys
import matplotlib.pylab as plt
from matplotlib.animation import FuncAnimation
from collections import Counter
from GOL_Class import GOL

#Create an instance of GOL
A = GOL(int(sys.argv[1]),str(sys.argv[2]))

#Animates the simulation of GOL if user selects
if sys.argv[3]=='viz':

    #Update plot function which sweeps the array and simulates the GOL
    def UpdatePlot(*args):
        image.set_array(A.array)
        A.Sweep()
        return image,

    #Animating the simulation. plt.imshow creates much faster moving animations so it is used here.
    GLImage = plt.figure()
    image = plt.imshow(A.array,animated=True)
    model = FuncAnimation(GLImage,UpdatePlot,interval=10,blit=True)
    plt.show()

#If user selects, simulates GOL for 200 Sweeps and calculates the velocity of the glider. NOTE: only works if initial condition is "glider"
elif sys.argv[3]=='data':
    t = 0
    tlist = []
    positionlist = []
    #Function to calculate absolute distance
    sq_dist = lambda x,y: np.sqrt(x**2. + y**2.)
    
    #Sweeps for 200 iterations and calculates COM
    for i in range(1000):
        A.Sweep()
        CoM = A.CoM()
        #If the COM of the glider is not near the boundaries, the time value and position are appended to lists
        if 3<CoM[0]<(A.dimension-3) and 3<CoM[1]<(A.dimension-3):
            t+=1
            if t%200==0:
                t = 0
            tlist.append(t)
            positionlist.append(sq_dist(CoM[0],CoM[1]))

    #Plots the position of the glider vs timestep.
    plt.plot(tlist[0:170],positionlist[0:170],'r:')
    plt.xlabel("Time (timesteps)")
    plt.ylabel("X Position in Array")
    plt.title("Plot of the X position of a Glider vs Timesteps")
    plt.show()

    #Calculates the velocity of the glider
    vel = GOL.Glider_Velocity(tlist[0:170],positionlist[0:170])
    print("The velocity of the glider is: {0:1.3f}".format(vel)+" indices/timestep")







    
    
    
    
    
