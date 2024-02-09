# Towards a Thermodynamical Deep-Learning-Vision-Based Flexible Robotic Cell for Circular Healthcare
This repository contains the source code and a demo video of the paper: Zocco, F., Sleath, D., and Rahimifard, S., 2024. Towards a thermodynamical deep-learning-vision-based flexible robotic cell for circular healthcare. arXiv preprint arXiv:2402.05551.  

## Overview of Files
* __MassDynamics.py__: Script to generate the numerical example of stock and flow dynamics and the circularity indicators covered in Section 3.2.
* __cellSimulator-v7.rdk__: RoboDK simulator of the cell, version 7. The simulator is still under development.
* __classifyMedDevices.ipynb__: Python notebook to be run on Jetson Nano for performing classification of medical devices.
* __screwTracking.ipynb__: Python notebook to be run on Jetson Nano for performing the tracking of screws on PCBs.   

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

**00:55-01:12**: Analogous to the previous part, with the only difference that the screw being tracked is located on the top-right corner
of the PCB.
