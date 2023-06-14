import socketio
import json

class ManualObject:
    '''
    The object that Pickle Rick has been inserted into, and is being tracked
    '''

    sio = socketio.Client(logger=False, engineio_logger=False)

    def __init__(self):
        self.off_n = 0
        self.off_e = 0
        self.off_d = 0
        self.ref_lat = 0
        self.ref_long = 0
        self.ref_alt = 0
     

    def set_pos(self, pos):
        self.off_n = pos
        

