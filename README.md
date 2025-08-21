# Shivanshu's RGB & Grayscale Image Visualizer

This is a simple and interactive **Streamlit web app** that allows users to visualize the RGB channels and grayscale version of a local image with customizable colormaps.

---

## 🔍 Features

- Load image from your **local file path**
- Visualize Red, Green, and Blue channels separately
- Convert image to **grayscale**
- Apply custom **Matplotlib colormaps** (`viridis`, `plasma`, `gray`, etc.)

---

## Project Files

```
image_channel_visualizer/
├── app.py               # Streamlit application file
├── README.md            # This documentation
└── my_image.jpg         # Local image file (you must add your own)
```

---

## How to Run This App

### 1. Install Required Libraries

```bash
pip install streamlit numpy pillow matplotlib
```

### 2. Update the Image Path

Edit `app.py` and change the image path inside the `load_image()` function:

```python
Image.open(r"C:\Users\dell\OneDrive\Desktop\my_image.jpg")
```

Replace it with your local image path.

### 3. Run the App

```bash
streamlit run app.py
```

Open your browser at [http://localhost:8501](http://localhost:8501)

---

## Dependencies

- Python 3.7+
- Streamlit
- NumPy
- Pillow (PIL)
- Matplotlib

---

## Author

Created by **Shivanshu Sahu**  
Full Stack AI & Data Science Learner

---

## Note

This version uses a **hardcoded local file path**. For public or online use, replace it with a `file_uploader` method.
