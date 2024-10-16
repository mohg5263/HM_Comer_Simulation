from setuptools import find_packages, setup

package_name = 'HM_COMER'

data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name + '/launch', ['launch/HM_COMER.py']))

data_files.append(('share/' + package_name + '/worlds', [
    'worlds/HM_COMER.wbt', 
]))
data_files.append(('share/' + package_name, ['package.xml']))
data_files.append(('share/' + package_name + '/resource', [
    'resource/HM_COMER.urdf',
    'resource/ros2control.yml',
]))

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=data_files,
    install_requires=['setuptools', 'launch'],
    zip_safe=True,
    maintainer='Mohammad Ghanatian',
    maintainer_email='mghanatian@crimson.ua.edu',
    description='Simulated environment for H.M. Comer Hall',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'launch.frontend.launch_extension': ['launch_ros = launch_ros'],    
        'console_scripts': ['HM_COMER = HM_COMER.HM_COMER:main']
    },

)
