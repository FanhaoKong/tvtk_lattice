#FCC Latticea
from tvtk.api import tvtk
from tvtk.tools import ivtk
from pyface.api import GUI
import numpy as np

a0=float(eval(input("Please input the lattice parameter:\n")))
unit=a0/2
rad=float(eval(input("Please input the radius of each atom:\n")))
number=int(eval(input("Please input the number of crytal cells on each edge:\n")))
lattice=tvtk.ImageData(origin=(-(number*unit),-(number*unit),-(number*unit)),spacing=(unit,unit,unit), \
                       dimensions=(2*number+1,2*number+1,2*number+1))
s,m,a=list(),list(),list()
count=int((number*2+1)**3)
for i in range(count):
    s.append(0); m.append(0); a.append(0)
    
for i in range(count):
    s[i]=tvtk.SphereSource(radius=rad,center=lattice.get_point(i), \
                theta_resolution=50,phi_resolution=50)
    m[i]=tvtk.PolyDataMapper(input_connection=s[i].output_port)
    a[i]=tvtk.Actor(mapper=m[i])
gui=GUI()
win=ivtk.IVTKWithCrustAndBrowser()
win.open()
point0=np.array(lattice.get_point(0))
for i in range(count):
    pointi=np.array(lattice.get_point(i))
    vector=pointi-point0
    if (int(np.sum(vector)/unit)%2==0):
        win.scene.add_actor(a[i])

dialog=win.control.centralWidget().widget(0).widget(0)
from pyface.qt import QtCore
dialog.setWindowFlags(QtCore.Qt.WindowFlags(0x00000000))
dialog.show()
gui.start_event_loop()








    
