#HCP lattice
import numpy as np
from tvtk.api import tvtk
from tvtk.tools import ivtk
from pyface.api import GUI
lista=list(map(eval,input("Please input a and c, separated by comma:\n").split(',')))
a,c=lista[0],lista[1]
rad=float(eval(input("Please input the radius of each atom:\n")))
number=int(eval(input("Please input the number of crytal cells on each edge:\n")))
vector1=np.array([a*np.sqrt(3.0)/2,-a/2.0,0.0])
vector2=np.array([0,a,0])
vector3=np.array([0,0,c])
trans=(1.0/3)*vector1+(2.0/3)*vector2+(1.0/2)*vector3
count=int((number+1)**3)
s,m,a,s2,m2,a2=list(),list(),list(),list(),list(),list()
for i in range(count):
    s.append(0);m.append(0);a.append(0);s2.append(0);m2.append(0);a2.append(0)
con=0
for i in range(number+1):
    for j in range(number+1):
        for k in range(number+1):
            point1=i*vector1+j*vector2+k*vector3
            point2=point1+trans
            s[con]=tvtk.SphereSource(radius=rad,center=tuple(point1), \
                theta_resolution=50,phi_resolution=50)
            s2[con]=tvtk.SphereSource(radius=rad,center=tuple(point2), \
                theta_resolution=50,phi_resolution=50)
            m[con]=tvtk.PolyDataMapper(input_connection=s[con].output_port)    
            m2[con]=tvtk.PolyDataMapper(input_connection=s2[con].output_port)
            a[con]=tvtk.Actor(mapper=m[con])
            a2[con]=tvtk.Actor(mapper=m2[con])
            a2[con].property.color=(1,1,0.4)
            con=con+1
gui=GUI()
win=ivtk.IVTKWithCrustAndBrowser()
win.open()

for i in range(count):
    win.scene.add_actor(a[i])
    win.scene.add_actor(a2[i])
    
print(a[0])

dialog=win.control.centralWidget().widget(0).widget(0)
from pyface.qt import QtCore
dialog.setWindowFlags(QtCore.Qt.WindowFlags(0x00000000))
dialog.show()
gui.start_event_loop()












