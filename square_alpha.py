#import rospy
import time
from threading import Timer
from point import Point
import pickle

def navigate_wait(x, y, z, speed, frame_id, tolerance=0.2):
    navigate(x=x, y=y, z=z, speed=speed, frame_id=frame_id, update_frame=True, auto_arm=False)

    while not rospy.is_shutdown():
        telem = get_telemetry(frame_id=frame_id)
        if get_distance(x, y, z, telem.x, telem.y, telem.z) < tolerance:
            break
        rospy.sleep(0.2)
class Aquaris():

    def __init__(self):
        self.out_of_water = False
        #self.cycle = 0
        #self.is_reserve = 0
        #self.subcycle = 0
        
    #def save_square(self,a,b,c):
        
    def out_of_water_trigger(self):
        print("OUT OF WATERn\n")
        self.out_of_water = True
    
    def square(self, a, b, c, cycles, load_save):
        p = Point(0,0)
        mapa = []
        
        while p.y < b:
            #print(p.x, p.y)
            mapa.append(Point(p.x, p.y))
            p.x = a
            #print(p.x, p.y)
            mapa.append(Point(p.x, p.y))
            p.y += c
            #print(p.x, p.y)
            mapa.append(Point(p.x, p.y))
            p.x = 0
            #print(p.x, p.y)
            mapa.append(Point(p.x, p.y))
            p.y += c
        #return mapa
        #navigate(x=0, y=0, z=2.0, speed=0.1, frame_id="fcu_horiz", update_frame=False, auto_arm=True)
        #time.sleep(4)
        #navigate_wait(x=0, y=0, z=2.0, speed=0.1, frame_id="aruco_map")
        is_res = 1
        timer = Timer(5.0, self.out_of_water_trigger)
        timer.start()
        for z in range(cycles):
            for i in range(len(mapa)):
                print(mapa[i])
        #        navigate_wait(x=mapa[i].x, y=mapa[i].y, z=2.0, speed=0.1, frame_id="aruco_map")
                if self.out_of_water:
                    print("DONG")
                    save = {}
                    save['cycles'] = cycles
                    save['cycle'] = z
                    save['is_reverse'] = is_res
                    save['subcycle'] = i
                    save['map'] = mapa
                    #print(save)
                    with open("save.pickle", "wb") as save_file:
                        pickle.dump(save, save_file)
                    print("DONG Dong")
                    return
                    
            mapa.reverse()
            is_res *= -1
            for i in range(len(mapa)):
                print(mapa[i])
        #        navigate_wait(x=point.x, y=point.y, z=2.0, speed=0.1, frame_id="aruco_map")
                if self.out_of_water:
                    print("DONG")
                    save = {}
                    save['cycles'] = cycles
                    save['cycle'] = z
                    save['is_reverse'] = is_res
                    save['subcycle'] = i
                    save['map'] = mapa
                    with open("save.pickle", "wb") as save_file:
                        pickle.dump(save, save_file)
                    print("DONG Dong")
                    return
        #    mapa.reverse()

A = Aquaris()
A.square(9,7.5,1,20,False)

d = {}
with open("save.pickle", "rb") as save_file:
    d = pickle.load(save_file)
print(d)
