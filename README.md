# HM_COMER Simulation

## Overview

This ROS2 package contains the ROS2 Webots simulation for the H.M. Comer Hall at the Univeristy of Alabama campus. The environment has adjustable parameters such as lighting intensity and doors that can be opened or closed. This documentation explains how to set up, run the simulation, and manipulate the parameters.

## Installation

To install and build this ROS2 package, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/mohg5263/HM_Comer_Simulation

   cd HM_COMER
    ```

2. Build the package:
   ```bash
     colcon build
     ```

3. Source the setup file:
   ```bash
    source install/setup.bash
    ```

## Running the Simulation
The simulation can be launched using the following command:

```bash
ros2 launch HM_COMER HM_COMER_Simulation.py
```

This will bring up the simulation environment with the default settings.

# Manipulating Parameters
The world file is located at  `HM_Comer_Simulation/HM_COMER/worlds
/HM_COMER.wbt` and we can manipulate the environment environmental factors such as lighting and door conditions as bellow:

## Lighting
You can adjust the lighting conditions in the simulation by changing the `pointLightIntensity` parameter in the ``HM_COMER.wbt`` file. To modify the lighting:

1. Open the `HM_COMER.wbt` launch file in the `worlds/` directory.

2. Locate the section where `FloorLight` object are defined.

3. Adjust the `pointLightIntensity` values as needed.

Example of modifying light intensity:

```bash
FloorLight {
  translation 5.54 8.44 0
  name "floor light(1)"
  #Change  the following line to modify light intensity of each light bulb
  pointLightIntensity 1.5   
}
```



## Doors
The simulation includes doors that can be opened or closed. You can control the state of the doors by setting the appropriate parameters in the simulation world file.

1. Navigate to the `worlds/` directory and open the `HM_COMER.wbt` world file.

2. Search for the `Door` object you wish to manipulate. Each door is identified by its object name, which you can find in the file.

3. Adjust the door’s properties to control its functionality and position. You can set the `canBeOpen` parameter to specify whether the door can be opened and modify the `position` parameter to define its angle.

Here's an example of how to configure door settings in the world file:

```bash
Door {
    translation 3.79006 -10.62 0
    rotation 0 0 1 1.5708
    size 0.2 2 4.2

    # Set to FALSE if the door should not be openable
    canBeOpen FALSE

    # Adjust the position to control the door's angle (in radians).
    # Set to 0 for a closed position or 1.57 for a fully opened position (90 degrees).
    position -1.0359379493002356

    frameHeight 3.5
    wallAppearance PorcelainChevronTiles {
    }
    doorHandle DoorLever {
        translation 0 0 -5.4892490687130646e-05
    }
}
```

### In this example:

- The `canBeOpen` property determines whether the door can be opened. Setting it to `FALSE` prevents the door from being opened during the simulation.
  
- The `position` value controls the angle of the door hinge. A value of `0` keeps the door closed, while `1.57` opens it to a 90-degree angle.


## Re-run the Simulation

After adjusting the door parameters, save your changes and re-run the simulation to see the updated door behaviors in action. 



