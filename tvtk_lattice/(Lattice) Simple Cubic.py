from tvtk.api import tvtk
from tvtk.tools import ivtk
from pyface.api import GUI

lattice=tvtk.ImageData(origin=(-5,-5,-5),spacing=(3,3,3), \
            dimensions=(10,10,10))
s,m,a=list(),list(),list()
for i in range(1000):
    s.append(0)
    m.append(0)
    a.append(0)
#for i in range(11):
#    print(type(lattice.get_point(i)))
for i in range(1000):
    if i%2==0:
        s[i]=tvtk.SphereSource(radius=1.0,center=lattice.get_point(i), \
                theta_resolution=50,phi_resolution=50,)
    else:
        s[i]=tvtk.SphereSource(radius=2.0,center=lattice.get_point(i), \
                theta_resolution=50,phi_resolution=50,)
    m[i]=tvtk.PolyDataMapper(input_connection=s[i].output_port)
    a[i]=tvtk.Actor(mapper=m[i])

gui=GUI()
win=ivtk.IVTKWithCrustAndBrowser()
win.open()
for i in range(1000):
    win.scene.add_actor(a[i])
    
dialog=win.control.centralWidget().widget(0).widget(0)
from pyface.qt import QtCore
dialog.setWindowFlags(QtCore.Qt.WindowFlags(0x00000000))
dialog.show()
gui.start_event_loop()