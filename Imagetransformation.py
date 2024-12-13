import cv2
import numpy as np
import streamlit as st
from matplotlib import pyplot as plt

# Function to apply brightness adjustment
def adjust_brightness(image, brightness=1.0):
    return np.clip(image * brightness, 0, 255).astype(np.uint8)

# Geometric transformations
def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, matrix, (w, h))

def scale_image(image, scale_factor):
    return cv2.resize(image, None, fx=scale_factor, fy=scale_factor)

def translate_image(image, tx, ty):
    matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    return cv2.warpAffine(image, matrix, (image.shape[1], image.shape[0]))

def skew_image(image, skew_x, skew_y):
    matrix = np.float32([[1, skew_x, 0], [skew_y, 1, 0]])
    return cv2.warpAffine(image, matrix, (image.shape[1], image.shape[0]))

# Streamlit UI
st.title("Image Processing App")

# Upload image
uploaded_file = st.file_uploader("Upload an image (PNG or JPEG)", type=["png", "jpeg"])

if uploaded_file is not None:
    # Load image
    image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)

    # Display original image
    st.subheader("Original Image")
    st.image(image, channels="BGR", use_column_width=True)

    # Brightness adjustment slider
    brightness = st.slider("Adjust Brightness", 0.0, 3.0, 1.0)
    bright_image = adjust_brightness(image, brightness)

    # Transformation sliders
    rotation_angle = st.slider("Rotation Angle", -180, 180, 0)
    scale_factor = st.slider("Scale Factor", 0.1, 3.0, 1.0)
    tx = st.slider("Translation X", -100, 100, 0)
    ty = st.slider("Translation Y", -100, 100, 0)
    skew_x = st.slider("Skew X", -1.0, 1.0, 0.0)
    skew_y = st.slider("Skew Y", -1.0, 1.0, 0.0)

    # Apply transformations
    rotated_image = rotate_image(bright_image, rotation_angle)
    scaled_image = scale_image(rotated_image, scale_factor)
    translated_image = translate_image(scaled_image, tx, ty)
    skewed_image = skew_image(translated_image, skew_x, skew_y)

    # Display transformed image
    st.subheader("Transformed Image")
    st.image(skewed_image, channels="BGR", use_column_width=True)

    # Save images (optional for later use)
    cv2.imwrite("output_image.png", skewed_image)
