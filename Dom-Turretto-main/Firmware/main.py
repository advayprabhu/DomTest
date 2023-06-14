from MO  import ManualObject
from turret import Turret
import time

pickle_rick = ManualObject()
dom_turretto = Turret(pickle_rick)

dom_turretto.set_heading(0)
dom_turretto.stepper_rig.set_gain(1,0.566666666666666)
#pickle_rick.connect_to_address("http://host:port/")


while True:
    pos = float(input('Enter off_n'))
    pickle_rick.set_pos(pos)
    dom_turretto.set_tgt()
    dom_turretto.update()
    time.sleep(10)
