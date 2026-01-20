from setuptools import find_packages, setup

package_name = 'kame_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
        'cmdvel_odom_node = kame_control.cmdvel_odom_node:main',
        'nav2_two_goals = kame_control.nav2_two_goals:main',
        'nav2_kadai = kame_control.nav2_kadai:main',
        'nav2_house = kame_control.nav2_house:main',
        ],
    },
)
