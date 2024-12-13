import cv2
import numpy as np
import streamlit as st
from matplotlib import pyplot as plt
from PIL import Image

def load_image(path):
    """Load an image from a file."""
    image = cv2.imread(path)
    if image is None:
        raise ValueError("Image not found. Please check the file path.")
    return image

def adjust_brightness(image, brightness_factor):
    """Adjust the brightness of the image."""
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv[..., 2] = hsv[..., 2] * brightness_factor
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

def rotate_image(image, angle):
    """Rotate an image by a specified angle."""
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, matrix, (w, h))
    return rotated

def scale_image(image, scale_x, scale_y):
    """Scale an image."""
    scaled = cv2.resize(image, None, fx=scale_x, fy=scale_y, interpolation=cv2.INTER_LINEAR)
    return scaled

def translate_image(image, tx, ty):
    """Translate an image."""
    (h, w) = image.shape[:2]
    matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    translated = cv2.warpAffine(image, matrix, (w, h))
    return translated

def skew_image(image, skew_x, skew_y):
    """Skew an image."""
    (h, w) = image.shape[:2]
    matrix = np.float32([[1, skew_x, 0], [skew_y, 1, 0]])
    skewed = cv2.warpAffine(image, matrix, (w, h))
    return skewed

# Streamlit Interface
st.title('Interactive Image Transformation')

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpeg", "jpg"])

if uploaded_file is not None:
    # Convert the uploaded file to an image
    image = Image.open(uploaded_file)
    image = np.array(image)

    # Display the original image
    st.image(image, caption='Original Image', use_column_width=True)

    # Brightness Adjustment
    brightness_factor = st.slider("Adjust Brightness", 0.0, 2.0, 1.0)
    adjusted_image = adjust_brightness(image, brightness_factor)

    # Transformation sliders
    rotation_angle = st.slider("Rotation Angle", -180, 180, 0)
    scale_x = st.slider("Scale X", 0.1, 3.0, 1.0)
    scale_y = st.slider("Scale Y", 0.1, 3.0, 1.0)
    translation_x = st.slider("Translate X", -200, 200, 0)
    translation_y = st.slider("Translate Y", -200, 200, 0)
    skew_x = st.slider("Skew X", -0.5, 0.5, 0.0)
    skew_y = st.slider("Skew Y", -0.5, 0.5, 0.0)

    # Apply transformations
    rotated_image = rotate_image(adjusted_image, rotation_angle)
    scaled_image = scale_image(rotated_image, scale_x, scale_y)
    translated_image = translate_image(scaled_image, translation_x, translation_y)
    skewed_image = skew_image(translated_image, skew_x, skew_y)

    # Display the transformed image
    st.image(skewed_image, caption='Transformed Image', use_column_width=True)

    # Provide options to download the transformed image
    _, download_button = st.columns([1, 2])
    with download_button:
        st.download_button(
            label="Download Transformed Image",
            data=cv2.imencode('.png', skewed_image)[1].tobytes(),
            file_name="transformed_image.png",
            mime="image/png"
        )
