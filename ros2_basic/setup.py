from setuptools import find_packages, setup
import os
from glob import glob
package_name = 'ros2_basic'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', 'ros2_basic', 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='s10',
    maintainer_email='aichitead25309@gmail',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        	'hello_node = ros2_basic.hello_node:main',
        	'cmd_vel_publisher = ros2_basic.cmd_vel_publisher:main',
        	'pose_subscriber = ros2_basic.pose_subscriber:main',
        	'wall_stop_controller = ros2_basic.wall_stop_controller:main',
        ],
    },
)
