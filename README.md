# 👁️‍🗨️ Human Monitoring with Classical Computer Vision

This repository provides a hands-on implementation of **classical computer vision algorithms** for **human detection and tracking**, using **Python** and **OpenCV**. It includes algorithms for feature extraction (SIFT, SURF, ORB), edge detection (Canny), human detection (HOG), and motion tracking (KLT). Each algorithm is modular, easy to understand, and accompanied by sample data and theoretical documentation.

---

## 🚀 Features

* 🧠 **Algorithms**:

  * Feature Extraction: `SIFT`, `SURF`, `ORB`
  * Edge Detection: `Canny`
  * Human Detection: `HOG`
  * Optical Flow Tracking: `KLT`

* 🎯 **Applications**:

  * Human surveillance
  * Crowd monitoring
  * Movement analysis

* 🧩 **Modular Code**:

  * Each algorithm in a separate Python script
  * Easy to modify and extend

* 🎞 **Sample Data**:

  * Images and videos for quick testing

* 📚 **Theoretical Documentation**:

  * Explanations of algorithms in `docs/`

---

## 📁 Repository Structure

```
HumanMonitoringCV/
├── README.md                 # Overview and usage guide
├── requirements.txt          # Python dependencies
├── src/                      # Source code for algorithms
│   ├── sift.py               # SIFT feature extraction
│   ├── surf.py               # SURF feature extraction
│   ├── orb.py                # ORB feature extraction
│   ├── canny.py              # Canny edge detection
│   ├── hog.py                # HOG human detection
│   ├── klt.py                # KLT optical flow tracking
│   └── demo.py               # Combined HOG + KLT demo
├── data/                     # Sample media files
│   ├── sample_image.jpg      # Example image (e.g., INRIA dataset)
│   ├── sample_video.mp4      # Example video (e.g., MOT16)
│   └── README.md             # How to download full datasets
├── docs/                     # Theory and algorithm explanations
│   ├── sift.md
│   ├── surf.md
│   ├── orb.md
│   ├── canny.md
│   ├── hog.md
│   └── klt.md
└── LICENSE                   # MIT License
```

---

## 🛠️ Prerequisites

* Python 3.8+
* OpenCV 4.5+
  *(Use `opencv-contrib-python` to access SIFT and SURF)*
* NumPy
* Optional: A webcam for real-time input

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/AliAkbariAlashti/Classical-Computer-Vision-Algorithms
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download sample datasets

See instructions in `data/README.md`. Sample files are already included for quick testing.

---

## ▶️ Usage

### Run individual algorithms

```bash
python src/orb.py --input data/sample_image.jpg
python src/hog.py --input data/sample_video.mp4
```

### Run the demo (HOG + KLT)

```bash
python src/demo.py --input data/sample_video.mp4
```

### Use real-time webcam input

```bash
python src/hog.py --webcam
```

> Press `q` to close OpenCV windows.

---

## 🎥 Datasets

* **INRIA Person Dataset**:
  For HOG-based human detection
  \[🔗 Download Link (add in `data/README.md`)]

* **MOT16 Dataset**:
  For motion tracking evaluation
  \[🔗 Download Link (add in `data/README.md`)]

---

## 🤝 Contributing

We welcome contributions of all kinds!

* 💡 Add new algorithms or enhancements
* 🐞 Report bugs or open issues
* 📄 Improve documentation

To contribute:

1. Fork the repository
2. Create a new branch (`feature/your-feature`)
3. Submit a pull request

---

## 📜 License

This project is licensed under the **MIT License**.
See the `LICENSE` file for more details.

---

## 🙌 Acknowledgments

This project is inspired by real-world needs for classical vision-based human monitoring — useful in surveillance, analytics, and educational applications.
