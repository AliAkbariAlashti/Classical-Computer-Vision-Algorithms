import cv2
import numpy as np
import argparse
import sys

def process_klt(image_path=None, use_webcam=False):
    """Process video with KLT optical flow tracking."""
    # KLT parameters
    lk_params = dict(winSize=(15, 15), maxLevel=2,
                     criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

    # Feature detection parameters for Shi-Tomasi corner detection
    feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)

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

    # Read first frame
    ret, old_frame = cap.read()
    if not ret:
        print("Error: Could not read first frame.")
        cap.release()
        sys.exit(1)

    old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
    p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

    # Create a mask for drawing tracks
    mask = np.zeros_like(old_frame)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Calculate optical flow
        p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

        # Select good points
        if p1 is not None:
            good_new = p1[st == 1]
            good_old = p0[st == 1]

            # Draw tracks
            for i, (new, old) in enumerate(zip(good_new, good_old)):
                a, b = new.ravel()
                c, d = old.ravel()
                mask = cv2.line(mask, (int(a), int(b)), (int(c), int(d)), (0, 255, 0), 2)
                frame = cv2.circle(frame, (int(a), int(b)), 5, (0, 0, 255), -1)

            # Overlay tracks on frame
            output = cv2.add(frame, mask)

            # Display result
            cv2.imshow('KLT Tracking', output)

            # Update previous frame and points
            old_gray = frame_gray.copy()
            p0 = good_new.reshape(-1, 1, 2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="KLT optical flow tracking for human monitoring.")
    parser.add_argument('--input', type=str, help="Path to input video.")
    parser.add_argument('--webcam', action='store_true', help="Use webcam as input.")
    args = parser.parse_args()

    try:
        process_klt(args.input, args.webcam)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
