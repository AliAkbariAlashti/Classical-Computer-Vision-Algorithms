````markdown
# 📄 HumanMonitoringCV – Classical Computer Vision Docs

Welcome to the `docs/` folder of the **HumanMonitoringCV** project!  
Here you'll find a collection of **concise, well-structured, and LaTeX-authored PDF documents** that explain the core theory and practical applications of classical computer vision algorithms used in this repository.

Each document offers:

✅ A brief theoretical overview (under 300 words)  
✅ Real-world applications in **human monitoring**  
✅ Implementation notes linked to the corresponding Python script in the `src/` folder  

These PDFs are perfect for quick reference or deeper understanding while working with the HumanMonitoringCV codebase.

---

## 📂 Available Documents

| File Name     | Description |
|---------------|-------------|
| `sift.pdf`    | **Scale-Invariant Feature Transform (SIFT)** – Robust feature detection across scales and rotations. |
| `surf.pdf`    | **Speeded-Up Robust Features (SURF)** – Fast and efficient alternative to SIFT. |
| `orb.pdf`     | **Oriented FAST and Rotated BRIEF (ORB)** – Lightweight, real-time friendly feature detection. |
| `canny.pdf`   | **Canny Edge Detection** – Precise and noise-resistant edge outlining. |
| `hog.pdf`     | **Histogram of Oriented Gradients (HOG)** – Widely used for **human detection** in static images. |
| `klt.pdf`     | **Kanade-Lucas-Tomasi (KLT) Tracker** – Reliable method for tracking motion through **optical flow**. |

All documents are written in **LaTeX** and compiled into **PDFs** for easy reading and high-quality formatting.

---

## 🛠️ How to Compile (Optional)

If you want to make changes or compile the documents yourself, follow these steps:

1. Make sure you have a LaTeX distribution installed (e.g., `TeX Live`, `MiKTeX`).
2. Navigate to the `docs/` folder in your terminal.
3. Run the following command:

```bash
latexmk -pdf <filename>.tex
````

🔧 Example:

```bash
latexmk -pdf hog.tex
```

This will generate `hog.pdf` using PDFLaTeX.
All documents use standard packages like `amsmath`, `enumitem`, and `lmodern`, available in most LaTeX distributions (especially `texlive-full`).

---

## 📘 Purpose

These documents are designed to support students, researchers, and developers working on **human monitoring systems**, providing both theoretical depth and practical insight.

---

📌 *Happy reading, and may your features be invariant and your edges sharp!*

```
