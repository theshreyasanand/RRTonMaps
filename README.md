# RRTonMaps
Just a simple code for applying the RRT Path Planning Algorithm on an actual map of IIT KGP Campus
# RRT Path Planning: IIT Kharagpur Campus Map

This project is a Python implementation of the Rapidly-exploring Random Tree (RRT) algorithm, specifically tailored to navigate a digital map of the IIT Kharagpur campus.

## Project Overview
The script simulates a pathfinding process by "growing" a tree of potential routes from a starting point. By randomly sampling the map and extending the tree toward those samples, it eventually finds a valid connection to the destination. It uses OpenCV to handle the image processing and to provide a real-time look at how the tree explores the campus.



### Core Features
* Landmark Selection: Choose between 11 preset locations including Nalanda, LBS, and the Main Building.
* Spatial Awareness: Uses image thresholding to distinguish between navigable paths and obstacles.
* Visual Feedback: Shows the tree expansion in green and highlights the final successful route in blue.

## Getting Started

### Prerequisites
You will need Python 3 installed along with the following libraries:
* NumPy: For coordinate math.
* OpenCV (cv2): For map processing and the visual interface.

You can install these via pip:
```bash
pip install numpy opencv-python
