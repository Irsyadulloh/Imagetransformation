import streamlit as st
from PIL import Image, ImageOps
import numpy as np

# Function to rotate the image
def rotate_image(img, angle):
    return img.rotate(angle)

# Function to scale (resize) the image
def scale_image(img, scale_factor):
    new_size = (int(img.width * scale_factor), int(img.height * scale_factor))
    return img.resize(new_size)

# Function to translate the image (apply offset) manually using numpy
def translate_image(img, x_offset, y_offset):
    img_array = np.array(img)  # Convert the image to a numpy array

    # Apply translation by shifting the array
    translated_array = np.roll(img_array, shift=(y_offset, x_offset), axis=(0, 1))

    # Convert the numpy array back to an image
    translated_img = Image.fromarray(translated_array)

    return translated_img

# Streamlit interface
st.title('Image Transformation with Streamlit')

# Upload image
uploaded_file = st.file_uploader("Choose an image", type=["png", "jpeg", "jpg"])

if uploaded_file is not None:
    # Open the image
    img = Image.open(uploaded_file)

    # Show original image
    st.image(img, caption="Original Image", use_column_width=True)

    # Add sliders for transformation
    rotate_angle = st.slider("Rotation Angle", min_value=0, max_value=360, step=1, value=0)
    scale_factor = st.slider("Scale Factor", min_value=0.1, max_value=2.0, step=0.1, value=1.0)
    x_offset = st.slider("Translation X Offset", min_value=-100, max_value=100, step=1, value=0)
    y_offset = st.slider("Translation Y Offset", min_value=-100, max_value=100, step=1, value=0)

    # Apply transformations
    rotated_image = rotate_image(img, rotate_angle)
    scaled_image = scale_image(img, scale_factor)
    translated_image = translate_image(img, x_offset, y_offset)

    # Show transformed images
    st.image(rotated_image, caption=f"Rotated by {rotate_angle}°", use_column_width=True)
    st.image(scaled_image, caption=f"Scaled by a factor of {scale_factor}", use_column_width=True)
    st.image(translated_image, caption=f"Translated by X: {x_offset}, Y: {y_offset}", use_column_width=True)
