import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import os


class TrafficSignDetector(Node):
    def __init__(self):
        super().__init__('traffic_sign_detector')

        self.publisher_ = self.create_publisher(String, 'traffic_sign', 10)

        # -------- MODEL --------
        self.model_path = "/mnt/c/Users/Priyanka Ramesh/Downloads/MAR_mp/final_model.h5"

        if not os.path.exists(self.model_path):
            self.get_logger().error("Model not found!")
            exit(1)

        self.model = load_model(self.model_path)
        self.get_logger().info("Model loaded successfully!")

        # -------- LABELS --------
        labels_path = "/mnt/c/Users/Priyanka Ramesh/Downloads/MAR_mp/labels.csv"

        if not os.path.exists(labels_path):
            self.get_logger().error("Labels file not found!")
            exit(1)

        self.labels = []
        with open(labels_path, 'r') as f:
            next(f)
            for line in f:
                parts = line.strip().split(",", 1)
                if len(parts) == 2:
                    _, name = parts
                    self.labels.append(name)

        self.get_logger().info(f"Loaded {len(self.labels)} labels")

        # -------- IMAGE FOLDER --------
        self.image_folder = "/mnt/c/Users/Priyanka Ramesh/Downloads/MAR_mp/test_images"

        if not os.path.exists(self.image_folder):
            self.get_logger().error("Image folder not found!")
            exit(1)

        # Load all image paths
        self.image_files = [
            os.path.join(self.image_folder, f)
            for f in os.listdir(self.image_folder)
            if f.lower().endswith(('.png', '.jpg', '.jpeg'))
        ]

        if len(self.image_files) == 0:
            self.get_logger().error("No images found in folder!")
            exit(1)

        self.get_logger().info(f"Loaded {len(self.image_files)} images")

        self.current_index = 0

        # Timer (change interval here)
        self.timer = self.create_timer(1.0, self.detect)

    def detect(self):
        # Get next image
        image_path = self.image_files[self.current_index]
        frame = cv2.imread(image_path)

        if frame is None:
            self.get_logger().error(f"Failed to load {image_path}")
            return

        # -------- PREPROCESS --------
        img = cv2.resize(frame, (32, 32))
        img = img / 255.0
        img = np.reshape(img, (1, 32, 32, 3))

        # -------- PREDICT --------
        pred = self.model.predict(img, verbose=0)
        class_id = int(np.argmax(pred))
        confidence = float(np.max(pred))

        # -------- LABEL --------
        if class_id < len(self.labels):
            result = self.labels[class_id]
        else:
            result = f"Unknown ({class_id})"

        # -------- ROS PUBLISH --------
        msg = String()
        msg.data = result
        self.publisher_.publish(msg)

        # -------- DISPLAY --------
        cv2.putText(
            frame,
            f"{result} ({confidence:.2f})",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

        cv2.imshow("Traffic Sign Detection", frame)
        cv2.waitKey(1)

        self.get_logger().info(f"{os.path.basename(image_path)} → {result} ({confidence:.2f})")

        # Move to next image
        self.current_index = (self.current_index + 1) % len(self.image_files)


def main(args=None):
    rclpy.init(args=args)
    node = TrafficSignDetector()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
