# 🚦 Traffic Sign Detection using ROS 2

## 📌 Overview

This project implements a **Traffic Sign Detection System** using a **Convolutional Neural Network (CNN)** integrated with **ROS 2**.

The system processes images in a continuous manner (simulating real-time input), classifies traffic signs using a trained deep learning model, and publishes the detected sign through a ROS topic.

---

## 🎯 Features

* 🤖 CNN-based traffic sign classification
* 🔄 Continuous image processing (folder-based simulation)
* 📡 ROS 2 publisher node for communication
* 🖼️ Real-time display with prediction and confidence
* 🧩 Modular and extendable architecture

---

## 🏗️ Project Structure

```
traffic_sign_project/
 ├── src/
 │    ├── traffic_sign_bot/
 │    │    ├── detector.py
 │    │    ├── final_model.h5
 │    │    └── ...
 │    
 │    
 │
 ├── test_images/
 ├── labels.csv
 └── README.md
```

---

## ⚙️ Technologies Used

* **ROS 2 (Humble)** – Communication framework
* **Python** – Core programming language
* **TensorFlow / Keras** – Model loading & prediction
* **OpenCV** – Image processing and display
* **NumPy** – Data preprocessing

---

## 🧠 Methodology

1. Load trained CNN model
2. Read images sequentially from a folder
3. Preprocess images (resize, normalize)
4. Predict class using model
5. Map prediction to label
6. Publish result to ROS topic (`/traffic_sign`)
7. Display output with confidence

---

## 🔄 System Workflow

```
Image Folder → Preprocessing → CNN Model → Prediction → ROS Topic → Display
```

---

## ▶️ How to Run

### 1️⃣ Clone the repository

```
git clone https://github.com/pryu24/traffic_sign_detector.git
cd traffic_sign_detector
```

---

### 2️⃣ Build the workspace

```
cd ~/ros2_ws
colcon build
```

---

### 3️⃣ Source the workspace

```
source install/setup.bash
```

---

### 4️⃣ Run the detector node

```
ros2 run traffic_sign_bot detector
```

---

### 5️⃣ View published data (optional)

Open another terminal:

```
ros2 topic echo /traffic_sign
```

---

## 📸 Output

* Displays detected traffic sign on screen
* Shows prediction confidence
* Publishes result to ROS topic

---

## ⚠️ Notes

* The system uses a **folder of images** to simulate real-time input
* Model expects images of size **32x32**
* Some class mismatch may exist depending on training dataset

---

## 🚀 Future Improvements

* 📷 Live camera integration
* 🎯 Object detection (bounding boxes)
* 🚗 Integration with autonomous navigation system
* 📡 ROS subscriber for decision making (Stop/Go actions)

---

## 👩‍💻 Authors

**Priyanka R, Rithvika Janani A, Rachana S,  Yuktha Pawar B**
GitHub: https://github.com/pryu24

---

## ⭐ Acknowledgment

This project is inspired by traffic sign recognition systems used in autonomous driving and intelligent transportation systems.
