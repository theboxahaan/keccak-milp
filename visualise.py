fp = open('Round1.sol', 'r')
raw_file = fp.readlines()
#create structures
A_list = [[0 for i in range(16)] for i in range(5)] # indexed A[j][k]
x_list = [[[0 for i in range(16)]for i in range(5)] for i in range(5)]
y_list = [[[0 for i in range(16)]for i in range(5)] for i in range(5)]
z_list = [[[0 for i in range(16)]for i in range(5)] for i in range(5)]

#parse sol file
for i in raw_file:
    p = i.split(' ')[0].split('_')
    if p[0] == 'x':
        x_list[int(p[2])][int(p[3])][int(p[4])] = int(i.split(' ')[1][:-1])
    if p[0] == 'A':
        A_list[int(p[2])][int(p[3])] = int(i.split(' ')[1][:-1])
    if p[0] == 'y':
        y_list[int(p[2])][int(p[3])][int(p[4])] = int(i.split(' ')[1][:-1])
    if p[0] == 'z':
        z_list[int(p[2])][int(p[3])][int(p[4])] = int(i.split(' ')[1][:-1])    


from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection='3d')
plt.xlabel('X')
plt.xticks()
plt.ylabel('Y')
plt.yticks()


#get z-data
zdata=[]
ydata=[]
xdata=[]
zcomp=[]
ycomp=[]
xcomp=[]

for i in range(5):
    for j in range(5):
        for k in range(16):
            if x_list[i][j][k] == 1 :
                zdata.append(k)
                ydata.append(j)
                xdata.append(i)
            else:
                zcomp.append(k)
                ycomp.append(j)
                xcomp.append(i)
ax.scatter3D(xdata, ydata, zdata, c="Blue");
ax.scatter3D(xcomp, ycomp, zcomp, c='Orange');
plt.show()
'''
for i in range(5):
    for j in range(5):
        for k in range(16):
            if y_list[i][j][k] == 1 :
                zdata.append(k)
                ydata.append(j)
                xdata.append(i)
            else:
                zcomp.append(k)
                ycomp.append(j)
                xcomp.append(i)
'''                
ax.scatter3D(xdata, ydata, zdata, c="Blue");
ax.scatter3D(xcomp, ycomp, zcomp, c='Orange');
plt.show()


