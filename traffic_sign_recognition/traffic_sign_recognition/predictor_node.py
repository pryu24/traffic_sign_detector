import rclpy
from rclpy.node import Node
from std_msgs.msg import String

import numpy as np
import cv2
from tensorflow.keras.models import load_model


class PredictorNode(Node):

    def __init__(self):
        super().__init__('predictor_node')

        self.publisher_ = self.create_publisher(String, 'traffic_sign', 10)

        self.model = load_model('/home/priy2005/ros2_ws/final_model.h5')

        self.timer = self.create_timer(2.0, self.predict_callback)

    def predict_callback(self):
        img = cv2.imread('/home/priy2005/ros2_ws/test.png')

        if img is None:
            self.get_logger().error("Image not found")
            return

        img = cv2.resize(img, (64, 64))
        img = img / 255.0
        img = np.expand_dims(img, axis=0)

        prediction = self.model.predict(img)
        label = str(np.argmax(prediction))

        msg = String()
        msg.data = label

        self.publisher_.publish(msg)
        self.get_logger().info(f'Predicted: {label}')


def main(args=None):
    rclpy.init(args=args)
    node = PredictorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
