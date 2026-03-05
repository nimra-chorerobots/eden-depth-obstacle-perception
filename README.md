# EDEN Depth-Aware Obstacle Perception Stack

A lightweight perception pipeline for outdoor robotics using RGB, instance segmentation, and depth estimation.

This project demonstrates **depth-aware obstacle detection for autonomous robots**, designed for environments such as lawns, parks, and outdoor terrain.

The system combines:

* RGB images
* Instance segmentation masks
* Depth maps

to detect objects and estimate their **distance from the robot**.

---

# Features

• Instance-based object detection from segmentation masks
• Depth-based distance estimation
• Heuristic object classification (Bush / Stone / Obstacle)
• Risk-aware visualization (safe / warning / danger)
• Real-time visualization pipeline

This approach is suitable for applications such as:

* Autonomous lawn mowing
* Outdoor delivery robots
* Snow removal robots
* Terrain monitoring systems
* Edge AI robotics

---

# Perception Pipeline

The system follows this processing pipeline:

RGB Image
↓
Instance Segmentation Mask
↓
Extract Object Instances
↓
Bounding Box Generation
↓
Depth ROI Extraction
↓
Distance Estimation
↓
Object Label Guessing
↓
Risk Visualization

---

# Example Output

The system detects terrain objects and estimates distance in centimeters.

Example detections include:

* Bush
* Stone
* Terrain obstacles

Each bounding box includes:

```
[label] [distance]
```

Example:

```
Bush 73cm
Obstacle 56cm
Stone 89cm
```

Color coding represents collision risk:

| Distance | Color  | Meaning            |
| -------- | ------ | ------------------ |
| < 30 cm  | Red    | Immediate obstacle |
| 30–60 cm | Orange | Medium risk        |
| > 60 cm  | Yellow | Safe distance      |

---

# Example Results

Example perception output from EDEN dataset.

```
<img width="793" height="600" alt="Screenshot_1" src="https://github.com/user-attachments/assets/4ee1d576-3ac1-481b-a8dd-f8a3cca72e8b" />
 
```
<img width="799" height="595" alt="Screenshot_4" src="https://github.com/user-attachments/assets/c03e9064-180c-4dce-8957-23ce99bc4251" />

---
<img width="802" height="600" alt="Screenshot_6" src="https://github.com/user-attachments/assets/5dc0b0f9-c26c-4b4f-92f5-b44c69abee17" />

---
---

# Dataset

The project uses the **EDEN dataset**, which contains:

* RGB images
* Instance segmentation maps
* Depth maps

---

# Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/eden-depth-obstacle-perception.git
cd eden-depth-obstacle-perception
```
 

# Running the Perception Stack

Run the script:

```
python src/eden_perception_v4.py
```

The system will:

1. Load RGB images
2. Extract objects from segmentation maps
3. Estimate object distances using depth maps
4. Display detections in real time

---

# Core Algorithms

### Instance Extraction

Objects are extracted using unique segmentation colors.

```
colors = np.unique(inst_img.reshape(-1,3),axis=0)
```

Each unique color corresponds to one object instance.

---

### Depth Estimation

Distance is estimated from the depth map using the ROI mean.

```
distance = mean(depth_roi)
```

---

### Object Label Guessing

A simple heuristic classifier uses HSV color statistics:

* Green → Bush
* Low saturation → Stone
* Otherwise → Obstacle

---

# Future Improvements

Possible improvements include:

• Replace heuristic labeling with semantic segmentation
• Use YOLO for object classification
• Fuse LiDAR + depth + stereo cameras
• Add terrain classification
• Integrate ROS2 perception pipeline
• Deploy on NVIDIA Jetson

---

# Robotics Applications

This system is suitable for perception modules in:

* Autonomous lawn mowers
* Snow removal robots
* Leaf vacuum robots
* Edge trimming robots
* Outdoor delivery robots

---

 
