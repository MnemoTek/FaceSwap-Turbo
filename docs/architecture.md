# Architecture Overview

## Pipeline

1. Video Input
2. Face Detection (InsightFace)
3. Embedding Extraction
4. Identity Matching (Cosine Similarity)
5. Face Swapping (ONNX model)
6. Video Rendering

## Key Components

- FaceAnalysis (detection + embeddings)
- ONNX Swapper Model
- Tkinter GUI
- OpenCV video pipeline

## Optimization

- CPU-only inference
- Frame-by-frame processing
- Efficient memory usage

## Limitations

- No temporal tracking
- Identity matching based on threshold
- CPU performance constraints
