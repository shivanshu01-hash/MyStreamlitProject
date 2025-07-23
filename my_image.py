import streamlit as st
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

st.set_page_config(page_title="My Image", layout="centered")
st.title("Shivanshu's Image - Multi-Color Channel Visualizer")

# Step 1: Load image from local path
@st.cache_data
def load_image():
    try:
        return Image.open(r"C:\Users\dell\OneDrive\Desktop\my_image.jpg").convert("RGB")
    except FileNotFoundError:
        st.error("❌ Image file not found at the specified path. Please check the path.")
        return None

shivanshu = load_image()

if shivanshu:
    # Step 2: Show original image
    st.image(shivanshu, caption="Original Image", use_container_width=True)

    # Step 3: Extract RGB channels
    shivanshu_np = np.array(shivanshu)
    R, G, B = shivanshu_np[:, :, 0], shivanshu_np[:, :, 1], shivanshu_np[:, :, 2]

    red_img = np.zeros_like(shivanshu_np)
    green_img = np.zeros_like(shivanshu_np)
    blue_img = np.zeros_like(shivanshu_np)

    red_img[:, :, 0] = R
    green_img[:, :, 1] = G
    blue_img[:, :, 2] = B

    # Step 4: Show RGB channel images
    st.subheader("RGB Channel Visualization")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(red_img, caption="Red Channel", use_container_width=True)

    with col2:
        st.image(green_img, caption="Green Channel", use_container_width=True)

    with col3:
        st.image(blue_img, caption="Blue Channel", use_container_width=True)

    # Step 5: Grayscale & Colormap
    st.subheader("Colormapped & Grayscale Image")
    colormap = st.selectbox(
        "🎨 Choose a Matplotlib colormap",
        ["viridis", "plasma", "inferno", "magma", "cividis", "hot", "cool", "gray"]
    )

    shivanshu_gray = shivanshu.convert("L")
    shivanshu_gray_np = np.array(shivanshu_gray)

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.imshow(shivanshu_gray_np, cmap=colormap)
    plt.axis("off")
    st.pyplot(fig)
