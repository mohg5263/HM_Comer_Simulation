# HM_COMER Simulation

## Overview

This ROS2 package contains the `HM_COMER` simulation for navigating and interacting with the H.M. Comer Hall at the Univeristy of Alabama. The environment has adjustable parameters such as lighting intensity and doors that can be opened or closed. This documentation explains how to set up, run the simulation, and manipulate the parameters.

## Installation

To install and build this ROS2 package, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/mohg5263/HM_Comer_Simulation
   cd HM_COMER

2. Build the package:
   ```bash
     colcon build

3. Source the setup file:
   ```bash
    source install/setup.bash

## Running the Simulation
You can launch the simulation using the following command:

```bash
ros2 launch HM_COMER HM_COMER_Simulation.py
```

This will bring up the simulation environment with the default settings.

# Manipulating Parameters
The `HM_COMER_Simulation` allows you to manipulate two key environmental factors:

## Lighting
You can adjust the lighting conditions in the simulation by changing the lighting parameter in the launch file. To modify the lighting:

1. Open the  `HM_COMER_Simulation.py` launch file in the `launch/` directory.

2. Locate the section where lighting parameters are defined.

3. Adjust the values as needed. For example, you can modify the intensity or direction of light sources.

## Doors
The simulation includes doors that can be opened or closed. You can control the state of the doors by setting the appropriate parameters in the simulation world file.

1. Open the world file in the `worlds/` directory.

2. Locate the doors you want to manipulate (identified by object names or tags).

3. Modify the `open` or `closed` states.
    ```bash
    # Example door control in the world file
    <Door>
    <State>open</State>
    </Door>

Adjust these values and re-run the simulation to see the changes.








