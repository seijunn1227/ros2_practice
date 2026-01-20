import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/s10/ros2_ws/src/ros2_practice/ros2_basic/install/ros2_basic'
