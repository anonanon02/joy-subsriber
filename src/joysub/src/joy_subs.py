#!/usr/bin/env python
  
import rospy
from std_msgs.msg import String, UInt16, Time, Float32, Int32
from sensor_msgs.msg import Joy
from time import sleep

#class subscribeto():
#    def __init__(self, msgs):
#        self.msgs = 



class Joy_sub:
    
    def __init__(self,axes,buttons):
        self.axes = axes
        self.buttons = buttons

    def callback(self,joy):
        self.axes = joy.axes
        self.buttons = joy.buttons
        
        

    def subs(self):
    
        rospy.init_node('joy_subs')
    
        rospy.Subscriber("joy", Joy , self.callback)
        sleep(0.5)
        return self.axes
        
  
if __name__ == '__main__':
    sub = Joy_sub(axes= 0,buttons = 0)
    a = sub.subs()
    print(a)
    rospy.spin()
    
    
   
