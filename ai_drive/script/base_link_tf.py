#!/usr/bin/env python  
import roslib
roslib.load_manifest('tf_pkg')
import rospy
import tf

 
if __name__ == '__main__':
     rospy.init_node('laser_tf_broadcaster')
     br=tf.TransformBroadcaster()
     br_odom=tf.TransformBroadcaster()
     rate=rospy.Rate(10.0)
     while not rospy.is_shutdown():
         br.sendTransform((-0.04,0.0,0.133),
         (0.0,0.0,0.0,1.0),rospy.Time.now(),"base_scan","base_link")

         br_odom.sendTransform((0.0,0.0,0.0),
         (0.0,0.0,0.0,1.0),rospy.Time.now(),"odom","base_link")
         rate.sleep()
         print("publishing... " )
     rospy.spin()
