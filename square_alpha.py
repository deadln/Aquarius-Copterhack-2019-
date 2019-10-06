#import rospy
import time
from threading import Timer
from point import Point




def navigate_wait(x, y, z, speed, frame_id, tolerance=0.2):
    navigate(x=x, y=y, z=z, speed=speed, frame_id=frame_id, update_frame=True, auto_arm=False)

    while not rospy.is_shutdown():
        telem = get_telemetry(frame_id=frame_id)
        if get_distance(x, y, z, telem.x, telem.y, telem.z) < tolerance:
            break
        rospy.sleep(0.2)
class Aquaris():

    def __init__(self):
        self.cycle = 0
        self.is_reserve = 0
        self.subcycle = 0
        
    def save_square(self,a,b,c):
        self.cycle = a
        
    
    def square(self, a, b, c, cycles, load_):
        p = Point(0,0)
        s = []
        
        while p.y < b:
            #print(p.x, p.y)
            s.append(Point(p.x, p.y))
            p.x = a
            #print(p.x, p.y)
            s.append(Point(p.x, p.y))
            p.y += c
            #print(p.x, p.y)
            s.append(Point(p.x, p.y))
            p.x = 0
            #print(p.x, p.y)
            s.append(Point(p.x, p.y))
            p.y += c
        return s
        #navigate(x=0, y=0, z=2.0, speed=0.1, frame_id="fcu_horiz", update_frame=False, auto_arm=True)
        #time.sleep(4)
        #navigate_wait(x=0, y=0, z=2.0, speed=0.1, frame_id="aruco_map")
        is_res = 1
        timer = Timer(20.0, HUI)
        for z in range(cycles):
        #    for point in s:
        #        navigate_wait(x=point.x, y=point.y, z=2.0, speed=0.1, frame_id="aruco_map")
            s.reverse()
            is_res *= -1
            for point in s:
        #        navigate_wait(x=point.x, y=point.y, z=2.0, speed=0.1, frame_id="aruco_map")
        #    s.reverse()

s = square(9,7.5,1,1)       
for i in s:
    print(i.x, i.y)
