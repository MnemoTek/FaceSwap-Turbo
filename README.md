# FaceSwap-Turbo
Fast multi-face swapping on CPU using InsightFace. Lightweight prototype with identity matching.
# FaceSwap Turbo

High-performance multi-face swapping on CPU.
A lightweight, identity-aware video processing system built for speed, scalability, and real-world deployment.



## Executive Summary

FaceSwap Turbo is a computer vision prototype designed to perform multi-face detection and identity-based face replacement in video streams, optimized to run efficiently on CPU-only environments.

Unlike traditional solutions that rely on GPU acceleration, this system demonstrates that face manipulation can be achieved with minimal hardware requirements, making it suitable for:

* Edge devices
* Low-cost deployments
* Scalable video processing pipelines



## Key Capabilities

* Multi-face detection
* Identity-aware face replacement using embedding similarity
* CPU-optimized inference pipeline
* Video processing support
* Lightweight graphical interface for rapid testing



## Core Technology

The system is built using:

* InsightFace (face detection and embeddings)
* ONNX Runtime (CPU inference)
* OpenCV (video processing)
* NumPy (vector operations)
* Tkinter (user interface)



## System Architecture

Pipeline overview:

1. Face detection on downscaled frames (performance optimization)
2. Extraction of normalized face embeddings
3. Identity matching via cosine similarity
4. Face swapping using ONNX-based model
5. Frame reconstruction and video encoding



## Performance Strategy

FaceSwap Turbo achieves efficiency through:

* Processing frames at reduced resolution
* Reprojecting coordinates to full resolution
* Avoiding GPU dependency
* Lightweight identity matching using vector similarity



## Prototype Status

This repository contains Version 1 (prototype).

The system has evolved internally through more than eight iterations, including:

* Identity stabilization across frames
* Performance optimizations
* Improved blending techniques
* Pipeline restructuring for scalability

Advanced versions are not publicly available.



## Demo

Add demo images or GIFs in the assets folder.



## Example Output

Add video preview in the videos folder.



## Use Cases

* Video editing and post-production
* Digital content creation
* Edge and mobile AI applications
* Research in identity-aware computer vision systems
* Real-time avatar systems (future direction)


## Competitive Positioning

| Feature             | FaceSwap Turbo |
| ------------------- | -------------- |
| CPU-only execution  | Yes            |
| Multi-face support  | Yes            |
| Identity matching   | Yes            |
| Lightweight         | Yes            |
| Real-time potential | In progress    |

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Usage

```bash
python app.py
```

---

## Dependencies

* opencv-python
* numpy
* pillow
* insightface
* onnxruntime

---

## Project Structure

```
FaceSwap-Turbo/
│
├── app.py
├── README.md
├── requirements.txt
├── assets/
├── videos/
└── docs/
```

---

## Limitations

* CPU-only execution (intentional for this version)
* Basic identity matching threshold
* No temporal smoothing
* Prototype-level interface

---

## Future Roadmap

* Optional GPU acceleration
* Temporal face tracking
* Improved blending techniques
* Real-time streaming support
* Model optimization (quantization, pruning)

---

## Investment and Collaboration

This project represents an early-stage prototype of a broader system focused on:

* Efficient AI-based video manipulation
* Scalable face-processing pipelines
* Edge-compatible computer vision systems

Open to research collaboration, funding opportunities, and product development partnerships.



## Author

MnemoTek



## Acknowledgments

Built using open-source tools, with a focus on the InsightFace ecosystem

