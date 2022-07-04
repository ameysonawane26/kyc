import streamlit as st
import numpy as np

st.title('KYC using AI')

st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

st.subheader("Image")
image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

st.image(image_file,width=250)
