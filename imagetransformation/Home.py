import streamlit as st

# Title and University Logo
st.title("University Logo & Project Description")

# Display the university logo
st.image("assets/university_logo.png", caption="University Logo", use_column_width=True)

# Project description
st.header("Project Description")
st.write("""
Welcome to our project. In this project, we will explore different image transformation techniques like:
- Rotation
- Scaling
- Translation
- Brightness adjustment

Each transformation will be interactive, allowing users to modify parameters via sliders and view the results in real-time.
""")

