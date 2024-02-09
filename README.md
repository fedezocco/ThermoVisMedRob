## Overview of Files

## Demo Video
A demo video is available at: https://vimeo.com/904066383?share=copy. It is made up of the following 4 parts.
**00:01-00:10**: Simulation of robot trajectories with the RoboDK cell simulator. The conveyor belt can be used in
the future for waste sorting simulations.  

**00:11-00:30**: The robotic arm moves on top of different medical devices. The camera is attached near the gripper.
The large screen inside the cell shows the camera view on the top-left side. Next to the camera view,
there is one vertical cursor per each object class: syringe, inhaler, and glucose meter. 
The neural network running on the Jetson Nano infers in real-time the object with the highest vertical cursor.

**00:31-00:54**: The robotic arm moves on top of the PCB of a glucose meter. The camera is attached near the robot flange.
The large screen inside the cell shows the camera view on the top-left side. The blue circle indicates the position
of one of the three screws. The cable is a disturbance and the main cause of the spikes in the tracking error as
the neural network was trained without it.

**00:55-01:12**: Analogous to Part 2, with the only difference that the screw being tracked is located on the top-right corner
of the PCB.
