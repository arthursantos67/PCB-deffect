from ultralytics import YOLO
import gradio as gr

model = YOLO('model/best.pt')

def detect_objects(image):
    results = model(image)

    annotated_image = results[0].plot()
    return annotated_image

iface = gr.Interface(
    fn=detect_objects,
    inputs=gr.Image(type="numpy", label="Upload a photo"),
    outputs=gr.Image(type="numpy", label="PCB board defect detected"),
    title="PCB Board Defect Detection",
    description="Upload an image to detect the defects on a PCB board"
)

iface.launch()