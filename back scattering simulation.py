import numpy as np
import math
import matplotlib.pyplot as plt

def val_int(core,y):
    core=int(core)
    L=math.sqrt((x_image-position[core-1][0])**2+(y-position[core-1][1])**2)
    return math.sin(2*pi/lda*(L+x_port))/L

def SaveData(list_x,list_y,directory):
    Q=input("Do you want to save the data? Y/N")
    if Q=="Y":
        filename=input("file name:")
        result_directory=directory+'\\'+filename+'.txt'
        print(result_directory)
        g=open(result_directory,'w')
        for x in list_x:
            g.write(str(x)+'\t'+str(list_y[list_x.index(x)])+'\n')
        g.close()

#parameter
lda=532/1000000000
theta=0#math.pi/2
d_cores=51/1000000
d_from_center=d_cores*math.sqrt(2)/2
pi=math.pi
directory="D:/USER/YJH/DATA/MCF back scattering"

position=[[d_from_center*math.cos(theta),d_from_center*math.sin(theta)],
          [d_from_center*math.cos(theta+pi/2),d_from_center*math.sin(theta+pi/2)],
          [d_from_center*math.cos(theta+pi),d_from_center*math.sin(theta+pi)],
          [d_from_center*math.cos(theta+pi*1.5),d_from_center*math.sin(theta+pi*1.5)]
          ]

x_port=100/1000000
x_image=300/1000

size_window=10/1000
numder_segment=1001
half_window=125#number

y_image=np.linspace(-size_window/2,size_window/2,numder_segment)
val_image=np.zeros(numder_segment)
y_image=y_image.tolist()
val_image=val_image.tolist()


for y in y_image:
    val_image[y_image.index(y)]=(val_int(1,y)+val_int(2,y)+val_int(3,y)+val_int(4,y))**2
    #val_image[y_image.index(y)]=(val_int(2,y)+val_int(4,y))**2

#SaveData(y_image,val_image,directory)

plt.plot(y_image,val_image)
plt.show()
