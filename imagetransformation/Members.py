import streamlit as st

# Title and Team Members Section
st.title("Our Team Members")

# Add a description
st.write("""
We are a group of passionate individuals from the University, working together to solve real-world problems with image processing.
""")

# Add team members and their photos (example for 3 members)
col1, col2, col3 = st.columns(3)

with col1:
    st.image("assets/member1.jpg", caption="Member 1", use_column_width=True)
    st.write("**Name:** John Doe\n**Role:** Developer")

with col2:
    st.image("assets/member2.jpg", caption="Member 2", use_column_width=True)
    st.write("**Name:** Jane Smith\n**Role:** Designer")

with col3:
    st.image("assets/member3.jpg", caption="Member 3", use_column_width=True)
    st.write("**Name:** Alice Johnson\n**Role:** Project Manager")

