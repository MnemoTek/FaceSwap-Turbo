import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np
from PIL import Image, ImageTk
import os

from insightface.app import FaceAnalysis
from insightface.model_zoo import get_model


# -----------------------------
# LOAD MODELS
# -----------------------------

print("Loading face detection model...")

app = FaceAnalysis(name="buffalo_l", providers=['CPUExecutionProvider'])
app.prepare(ctx_id=0, det_size=(640, 640))

print("Loading face swap model...")

swapper = get_model(
    r"C:\Users\hp\.insightface\models\inswapper_128.onnx",
    providers=['CPUExecutionProvider']
)

print("Models loaded successfully.")


# -----------------------------
# GUI
# -----------------------------

class FaceSwapStudio:

    def __init__(self, root):

        self.root = root
        self.root.title("FaceSwap Studio (Local CPU)")
        self.root.geometry("800x600")

        self.video_path = None
        self.output_path = "output_swapped.mp4"

        self.face_images = {}

        # VIDEO BUTTON
        tk.Button(root, text="Load Video", command=self.load_video).pack(pady=10)

        # DETECT BUTTON
        tk.Button(root, text="Detect Faces", command=self.detect_faces).pack(pady=10)

        # FACE REPLACEMENT
        self.face_frame = tk.Frame(root)
        self.face_frame.pack(pady=10)

        # RENDER BUTTON
        tk.Button(root, text="Render FaceSwap", command=self.render_video).pack(pady=20)

        # STATUS
        self.status = tk.Label(root, text="Status: Waiting")
        self.status.pack()

    # -----------------------------
    # LOAD VIDEO
    # -----------------------------

    def load_video(self):

        self.video_path = filedialog.askopenfilename(
            filetypes=[("Video files", "*.mp4 *.avi *.mov")]
        )

        if self.video_path:
            self.status.config(text=f"Video loaded: {self.video_path}")

    # -----------------------------
    # DETECT FACES
    # -----------------------------

    def detect_faces(self):

        if not self.video_path:
            self.status.config(text="Load video first")
            return

        cap = cv2.VideoCapture(self.video_path)
        ret, frame = cap.read()
        cap.release()

        if not ret:
            self.status.config(text="Error reading video")
            return

        faces = app.get(frame)

        for widget in self.face_frame.winfo_children():
            widget.destroy()

        for i, face in enumerate(faces):

            frame_row = tk.Frame(self.face_frame)
            frame_row.pack(pady=5)

            tk.Label(frame_row, text=f"Face {i+1}").pack(side=tk.LEFT)

            btn = tk.Button(
                frame_row,
                text="Upload replacement image",
                command=lambda i=i: self.load_face_image(i)
            )
            btn.pack(side=tk.LEFT)

        self.faces_detected = faces

        self.status.config(text=f"{len(faces)} faces detected")

    # -----------------------------
    # LOAD FACE IMAGE
    # -----------------------------

    def load_face_image(self, index):

        path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.png")]
        )

        if path:

            img = cv2.imread(path)
            faces = app.get(img)

            if len(faces) == 0:
                self.status.config(text="No face found in image")
                return

            self.face_images[index] = faces[0]

            self.status.config(text=f"Image assigned to Face {index+1}")

    # -----------------------------
    # RENDER VIDEO
    # -----------------------------

    def render_video(self):

        if not self.video_path:
            self.status.config(text="Load video first")
            return

        cap = cv2.VideoCapture(self.video_path)

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(self.output_path, fourcc, fps, (width, height))

        frame_count = 0

        while True:

            ret, frame = cap.read()

            if not ret:
                break

            faces = app.get(frame)

            for i, face in enumerate(faces):

                if i in self.face_images:

                    frame = swapper.get(
                        frame,
                        face,
                        self.face_images[i],
                        paste_back=True
                    )

            out.write(frame)

            frame_count += 1

            if frame_count % 10 == 0:
                print("Processed frames:", frame_count)

        cap.release()
        out.release()

        self.status.config(text="Render finished → output_swapped.mp4")

        print("Video saved:", self.output_path)


# -----------------------------
# RUN GUI
# -----------------------------

root = tk.Tk()
app_gui = FaceSwapStudio(root)
root.mainloop()
