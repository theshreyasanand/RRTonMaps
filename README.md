# RRT Path Planning: IIT Kharagpur Campus Map

This project is a Python implementation of the Rapidly-exploring Random Tree (RRT) algorithm, specifically tailored to navigate a digital map of the IIT Kharagpur campus.

## Project Overview
The script simulates a pathfinding process by "growing" a tree of potential routes from a starting point. By randomly sampling the map and extending the tree toward those samples, it eventually finds a valid connection to the destination. It uses OpenCV to handle the image processing and to provide a real-time look at how the tree explores the campus.


### Core Features
* Landmark Selection: Choose between 11 preset locations including Nalanda, LBS, and the Main Building.
* Spatial Awareness: Uses image thresholding to distinguish between navigable paths and obstacles.
* Visual Feedback: Shows the tree expansion in green and highlights the final successful route in blue.

## Project Structure
```text
RRTonMaps/
├── assets/
│   └── Map of IIT KGP.png    # Campus map png file
├── src/
│   └── RRTonKGP.py           # Main path planning script
├── README.md                 # Project documentation
└── requirements.txt          # Python dependencies
```

## Getting Started

### Prerequisites
You will need Python 3 installed. All required libraries (NumPy, OpenCV, Matplotlib) are listed in the `requirements.txt` file.

You can install all of them at once by running:
```bash
pip install -r requirements.txt
```

### Setup and Execution
1. Ensure your folder structure matches the layout shown in the Project Structure section above.
2. Navigate to the project root directory in your terminal.
3. Run the program using the following command:
   ```bash
   python src/RRTonKGP.py
   ```
4. When prompted in the terminal, enter the serial numbers for your starting point and your destination.

## How the Algorithm Works
1. **Sampling:** The code picks a random coordinate on the map.
2. **Extension:** It identifies the closest existing point in the tree and moves a small step (7 pixels) toward the new random coordinate.
3. **Validation:** It checks every pixel along that new segment to ensure it doesn't cross a building or obstacle.
4. **Completion:** Once a branch gets within 15 pixels of the target, the search stops.
5. **Backtracking:** The script then traces the lineage of the successful branch back to the start to draw the final path.