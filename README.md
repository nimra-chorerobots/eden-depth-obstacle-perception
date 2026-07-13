# Chore Depth-Aware Obstacle Perception

### RGB, Instance Segmentation, and Depth-Based Obstacle Perception for Outdoor Robotics

This repository implements a lightweight **depth-aware obstacle perception pipeline** for outdoor robotics using RGB imagery, instance segmentation, and depth estimation. It is designed to identify terrain obstacles, estimate their distance from the robot, and provide an interpretable visualization suitable for autonomous navigation.

The system demonstrates how perception outputs from RGB images, segmentation masks, and depth maps can be combined to generate spatial awareness for robots operating in outdoor environments such as lawns, parks, sidewalks, and natural terrain.

---

# 📌 Overview

Reliable obstacle perception is essential for autonomous outdoor robots operating in dynamic environments. While RGB images provide semantic information, depth maps enable spatial understanding, allowing robots to estimate obstacle distance and navigation risk.

This repository demonstrates a complete perception pipeline that integrates:

- RGB image processing
- Instance segmentation
- Object extraction
- Depth estimation
- Distance measurement
- Heuristic object classification
- Risk-aware visualization

The repository is intended for:

- Outdoor robotics
- Autonomous lawn mowing
- Snow removal robots
- Delivery robots
- Computer vision research
- Robotics education
- Edge AI perception
- Navigation research

---

# 🚀 Features

- RGB image processing
- Instance segmentation-based object extraction
- Depth-based distance estimation
- Bounding-box generation
- Heuristic object classification
- Risk-aware obstacle visualization
- Real-time perception pipeline
- Lightweight implementation suitable for embedded systems

---

# 📂 Dataset

This project uses the **EDEN Dataset**, which provides synchronized perception data for outdoor robotic environments.

The dataset includes:

- RGB images
- Instance segmentation masks
- Depth maps

These modalities enable object extraction, obstacle localization, and depth-aware perception.

Example dataset structure:

```text
EDEN/
├── rgb/
├── depth/
├── instance_masks/
└── annotations/
```

---

# 🔄 Processing Pipeline

```text
RGB Image
      │
      ▼
Instance Segmentation
      │
      ▼
Extract Object Instances
      │
      ▼
Bounding Box Generation
      │
      ▼
Depth ROI Extraction
      │
      ▼
Distance Estimation
      │
      ▼
Object Classification
      │
      ▼
Risk Visualization
```

---

# ⚙️ Core Components

## 1️⃣ RGB Image Processing

The RGB image provides the visual appearance of the environment and serves as the reference image for obstacle visualization.

---

## 2️⃣ Instance Segmentation

Objects are extracted from instance segmentation masks, where each unique color corresponds to a different object.

Outputs include:

- Individual object instances
- Object masks
- Bounding boxes

---

## 3️⃣ Distance Estimation

Depth values inside each object region are used to estimate the object's distance from the robot.

Outputs include:

- Estimated distance
- Relative obstacle position
- Collision awareness

---

## 4️⃣ Object Classification

A lightweight heuristic classifier categorizes detected objects using HSV color statistics.

Example classes:

- Bush
- Stone
- Obstacle

This module can later be replaced with a deep-learning object detector.

---

## 5️⃣ Risk Visualization

Each detected object is visualized together with:

- Object label
- Estimated distance
- Bounding box
- Collision risk color

Risk levels:

| Distance | Color | Meaning |
|----------|--------|----------------------|
| <30 cm | 🔴 Red | Immediate obstacle |
| 30–60 cm | 🟠 Orange | Medium risk |
| >60 cm | 🟡 Yellow | Safe distance |

---

# 🖥 Visualization Results

The following examples demonstrate the depth-aware perception pipeline on representative scenes from the EDEN dataset.

---

## Example 1 — Outdoor Terrain Perception

<img width="793" height="600" alt="Screenshot_1" src="https://github.com/user-attachments/assets/4ee1d576-3ac1-481b-a8dd-f8a3cca72e8b" />

The perception pipeline detects nearby vegetation and terrain obstacles while estimating their distance from the robot.

---

## Example 2 — Bush and Obstacle Detection

<img width="799" height="595" alt="Screenshot_4" src="https://github.com/user-attachments/assets/c03e9064-180c-4dce-8957-23ce99bc4251" />

Depth-aware visualization highlighting multiple objects with estimated distances.

---

## Example 3 — Terrain Object Localization

<img width="802" height="600" alt="Screenshot_6" src="https://github.com/user-attachments/assets/5dc0b0f9-c26c-4b4f-92f5-b44c69abee17" />

Visualization of segmented terrain obstacles together with estimated distances and navigation risk.

---

# 📈 Representative Capabilities

The perception pipeline demonstrates:

- Instance-based object extraction
- Depth-aware obstacle localization
- Relative distance estimation
- Lightweight object classification
- Collision-risk visualization
- Outdoor terrain understanding
- Real-time visualization

---

# 🏗 Architecture

```text
RGB Image
      │
      ▼
Instance Segmentation
      │
      ▼
Object Extraction
      │
      ▼
Depth Estimation
      │
      ▼
Distance Measurement
      │
      ▼
Object Classification
      │
      ▼
Risk Assessment
      │
      ▼
Visualization
```

---

# 🚀 Project Status

🟢 **Prototype**

### Current Features

- RGB image processing
- Instance segmentation
- Object extraction
- Distance estimation
- Bounding-box generation
- Risk-aware visualization
- Lightweight heuristic classifier

### Planned Improvements

- YOLOv8 object detection
- Semantic segmentation
- Camera–LiDAR fusion
- ROS 2 integration
- NVIDIA Isaac Sim integration
- Jetson deployment
- Dynamic obstacle tracking
- Navigation interface

---

# 📂 Repository Structure

```text
chore-depth-aware-perception/
│
├── src/
│   └── eden_perception_v4.py
│
├── assets/
│   ├── input/
│   ├── output/
│   └── examples/
│
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
├── CHANGELOG.md
├── CITATION.cff
└── CONTRIBUTING.md
```

---

# ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/nimra-chorerobots/chore-depth-aware-perception.git

cd chore-depth-aware-perception
```

Install dependencies:

```bash
pip install -r requirements.txt
```

or

```bash
pip install numpy opencv-python matplotlib scikit-image
```

---

# 📦 Requirements

- Python 3.9+
- NumPy
- OpenCV
- Matplotlib
- scikit-image

Example `requirements.txt`

```text
numpy
opencv-python
matplotlib
scikit-image
```

---

# ▶️ Running the Project

Run the perception pipeline:

```bash
python src/eden_perception_v4.py
```

The system performs the following steps:

1. Load RGB images
2. Load segmentation masks
3. Extract object instances
4. Estimate object distances
5. Generate bounding boxes
6. Visualize obstacle locations
7. Display risk-aware perception results

---

# 💡 Applications

This repository can be used for:

- Autonomous lawn mowing
- Outdoor mobile robotics
- Snow removal robots
- Delivery robots
- Terrain monitoring
- Computer vision research
- Edge AI
- Robotics education
- Autonomous navigation

---

# 🔮 Future Work

Future versions of this repository will include:

- YOLOv8 integration
- Semantic segmentation
- Camera–LiDAR fusion
- ROS 2 perception nodes
- NVIDIA Isaac Sim integration
- Real-time deployment
- Terrain classification
- Navigation planning
- Dynamic obstacle tracking

 
