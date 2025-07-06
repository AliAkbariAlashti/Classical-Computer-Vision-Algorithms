import cv2
import numpy as np
import argparse
import sys

def process_demo(image_path=None, use_webcam=False):
    """Demo combining HOG human detection and KLT tracking."""
    # Initialize HOG
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # Initialize KLT parameters
    lk_params = dict(winSize=(15, 15), maxLevel=2,
                     criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

    if use_webcam:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Could not open webcam.")
            sys.exit(1)
    else:
        if not image_path:
            print("Error: Please provide a video path.")
            sys.exit(1)
        cap = cv2.VideoCapture(image_path)
        if not cap.isOpened():
            print(f"Error: Could not open file {image_path}.")
            sys.exit(1)

    # Initialize tracking points
    old_gray = None
    p0 = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (640, 480))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # HOG detection every 10 frames
        if p0 is None or len(p0) == 0:
            boxes, weights = hog.detectMultiScale(frame, winStride=(8, 8), padding=(8, 8), scale=1.05)
            if len(boxes) > 0:
                # Use center of first detected human as tracking point
                x, y, w, h = boxes[0]
                p0 = np.array([[x + w // 2, y + h // 2]], dtype=np.float32).reshape(-1, 1, 2)
                old_gray = gray.copy()

        # KLT tracking
        if p0 is not None and old_gray is not None:
            p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, gray, p0, None, **lk_params)
            if p1 is not None and st.any():
                for i, (new, old) in enumerate(zip(p1, p0)):
                    if st[i]:
                        a, b = new.ravel()
                        c, d = old.ravel()
                        cv2.line(frame, (int(a), int(b)), (int(c), int(d)), (0, 255, 0), 2)
                        cv2.circle(frame, (int(a), int(b)), 5, (0, 0, 255), -1)
                p0 = p1[st == 1].reshape(-1, 1, 2)
                old_gray = gray.copy()

        cv2.imshow('HOG + KLT Demo', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Combined HOG and KLT demo for human monitoring.")
    parser.add_argument('--input', type=str, help="Path to input video.")
    parser.add_argument('--webcam', action='store_true', help="Use webcam as input.")
    args = parser.parse_args()

    try:
        process_demo(args.input, args.webcam)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
