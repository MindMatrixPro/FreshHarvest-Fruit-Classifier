from model_helper import predict
from PIL import Image
import base64
import os
os.environ["STREAMLIT_SERVER_FILEWATCHER_TYPE"] = "none"
import streamlit as st

st.set_page_config(page_title="Fruit Classifier 🍍", page_icon="🍍", layout="centered")

st.title("🍓 Fruit Classification Demo")
st.write("Upload an image of a fruit, and the model will predict its category.")

uploaded_file = st.file_uploader("Drag and Drop or Browse an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image_path = "temp_image.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Determine orientation
    img = Image.open(image_path)
    width, height = img.size
    is_landscape = width >= height

    # Convert image to base64 for display
    buffered = open(image_path, "rb")
    img_bytes = buffered.read()
    encoded = base64.b64encode(img_bytes).decode()

    display_width = 500 if is_landscape else 300

    st.markdown(
        f"""
        <div style="text-align:center;">
            <img src="data:image/jpeg;base64,{encoded}" width="{display_width}" style="margin-bottom: 10px;" />
        </div>
        """,
        unsafe_allow_html=True
    )

    # Predict
    prediction = predict(image_path)
    st.success(f"**Predicted Class:** {prediction}")
