#!/usr/bin/env python
  
import rospy
from std_msgs.msg import String, UInt16, Time, Float32, Int32
from sensor_msgs.msg import Joy

#class subscribeto():
#    def __init__(self, msgs):
#        self.msgs = 



class Joy_sub:
    
    def __init__(self):

        sub_topic = 'joy'

        self.axes = rospy.Subscriber(sub_topic, Joy , self.axes_addition)

    def axes_callback(self, msg):
        return msg.axes

    def buttons_callback(self, msg):
        return msg.buttons

    def axes_addition(self, msg):
        axes = self.axes_callback(msg)
        buttons = self.buttons_callback(msg)
        x = 0
        for i in range(len(axes)):
            x += axes[i] + buttons[i]
        
        if x >= 5:
            print(axes)
            print(buttons)
            print('greater than or equal to 5')
            print()
        else:
            print(axes)
            print(buttons)
            print('less than 5')
            print()



  
if __name__ == '__main__':
    rospy.init_node('joy_subs')
    sub = Joy_sub()

    rospy.spin()
    
   
