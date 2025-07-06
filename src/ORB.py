import cv2
import numpy as np
import argparse
import sys

def process_orb(image_path=None, use_webcam=False):
    """Process image or video with ORB feature detection."""
    # Initialize ORB detector
    orb = cv2.ORB_create(nfeatures=1000)

    if use_webcam:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Could not open webcam.")
            sys.exit(1)
    else:
        if not image_path:
            print("Error: Please provide an image or video path.")
            sys.exit(1)
        cap = cv2.VideoCapture(image_path)
        if not cap.isOpened():
            print(f"Error: Could not open file {image_path}.")
            sys.exit(1)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect keypoints and descriptors
        keypoints, descriptors = orb.detectAndCompute(gray, None)

        # Draw keypoints
        output = cv2.drawKeypoints(frame, keypoints, None, color=(0, 255, 0), flags=0)

        # Display result
        cv2.imshow('ORB Keypoints', output)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ORB feature detection for human monitoring.")
    parser.add_argument('--input', type=str, help="Path to input image or video.")
    parser.add_argument('--webcam', action='store_true', help="Use webcam as input.")
    args = parser.parse_args()

    try:
        process_orb(args.input, args.webcam)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
