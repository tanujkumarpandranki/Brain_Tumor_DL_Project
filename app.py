<<<<<<< HEAD
import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# ==========================
# PAGE CONFIG
# ==========================
st.set_page_config(page_title="Brain Tumor Classifier", page_icon="🧠", layout="centered")

# ==========================
# LOAD MODEL (cache for speed)
# ==========================
@st.cache_resource
def load_my_model():
    return load_model("brain_tumor_model (3).h5")

model = load_my_model()

class_names = ['glioma', 'meningioma', 'no_tumor', 'pituitary']

# ==========================
# UI
# ==========================
st.title("🧠 Brain Tumor Classifier")
st.write("Upload an MRI image to detect tumor type")

uploaded_file = st.file_uploader("Choose Image", type=["jpg","png","jpeg"])

if uploaded_file is not None:

    img = Image.open(uploaded_file).convert('RGB')

    # Display image
    st.image(img, caption="Uploaded Image", use_container_width=True)

    # ==========================
    # PREPROCESSING
    # ==========================
    img = img.resize((224, 224)) 
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # ==========================
    # PREDICTION
    # ==========================
    with st.spinner("Analyzing MRI..."):
        prediction = model.predict(img_array)

    index = np.argmax(prediction)
    confidence = float(np.max(prediction)) * 100
    result = class_names[index]

    # ==========================
    # RESULT
    # ==========================
    st.subheader("🔍 Result")
    st.write(f"**Prediction:** {result.upper()}")
    st.write(f"**Confidence:** {confidence:.2f}%")

    # Progress bar for confidence
    st.progress(int(confidence))

    # ==========================
    # DIAGNOSIS + SUGGESTIONS
    # ==========================
    st.subheader("🩺 Diagnosis & Suggestions")

    if confidence < 70:
        st.warning("⚠️ Low confidence. Please upload a clearer MRI image.")

    elif result == "glioma":
        st.error("Glioma tumor detected")
        st.write("👉 Consult a neurologist immediately.")
        st.write("👉 MRI/CT scan follow-up and biopsy may be required.")

    elif result == "meningioma":
        st.warning("Meningioma tumor detected")
        st.write("👉 Visit a specialist for evaluation.")
        st.write("👉 Regular monitoring is recommended.")

    elif result == "no_tumor":
        st.success("No tumor detected")
        st.write("👉 Maintain a healthy lifestyle.")
        st.write("👉 Regular checkups if symptoms persist.")

    elif result == "pituitary":
        st.warning("Pituitary tumor detected")
        st.write("👉 Consult an endocrinologist.")
        st.write("👉 Hormone tests + MRI recommended.")

# ==========================
# FOOTER
# ==========================
st.markdown("---")
=======
import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# ==========================
# PAGE CONFIG
# ==========================
st.set_page_config(page_title="Brain Tumor Classifier", page_icon="🧠", layout="centered")

# ==========================
# LOAD MODEL (cache for speed)
# ==========================
@st.cache_resource
def load_my_model():
    return load_model("brain_tumor_model (3).h5")

model = load_my_model()

class_names = ['glioma', 'meningioma', 'no_tumor', 'pituitary']

# ==========================
# UI
# ==========================
st.title("🧠 Brain Tumor Classifier")
st.write("Upload an MRI image to detect tumor type")

uploaded_file = st.file_uploader("Choose Image", type=["jpg","png","jpeg"])

if uploaded_file is not None:

    img = Image.open(uploaded_file).convert('RGB')

    # Display image
    st.image(img, caption="Uploaded Image", use_container_width=True)

    # ==========================
    # PREPROCESSING
    # ==========================
    img = img.resize((224, 224)) 
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # ==========================
    # PREDICTION
    # ==========================
    with st.spinner("Analyzing MRI..."):
        prediction = model.predict(img_array)

    index = np.argmax(prediction)
    confidence = float(np.max(prediction)) * 100
    result = class_names[index]

    # ==========================
    # RESULT
    # ==========================
    st.subheader("🔍 Result")
    st.write(f"**Prediction:** {result.upper()}")
    st.write(f"**Confidence:** {confidence:.2f}%")

    # Progress bar for confidence
    st.progress(int(confidence))

    # ==========================
    # DIAGNOSIS + SUGGESTIONS
    # ==========================
    st.subheader("🩺 Diagnosis & Suggestions")

    if confidence < 70:
        st.warning("⚠️ Low confidence. Please upload a clearer MRI image.")

    elif result == "glioma":
        st.error("Glioma tumor detected")
        st.write("👉 Consult a neurologist immediately.")
        st.write("👉 MRI/CT scan follow-up and biopsy may be required.")

    elif result == "meningioma":
        st.warning("Meningioma tumor detected")
        st.write("👉 Visit a specialist for evaluation.")
        st.write("👉 Regular monitoring is recommended.")

    elif result == "no_tumor":
        st.success("No tumor detected")
        st.write("👉 Maintain a healthy lifestyle.")
        st.write("👉 Regular checkups if symptoms persist.")

    elif result == "pituitary":
        st.warning("Pituitary tumor detected")
        st.write("👉 Consult an endocrinologist.")
        st.write("👉 Hormone tests + MRI recommended.")

# ==========================
# FOOTER
# ==========================
st.markdown("---")
>>>>>>> 02421059944a2319616f2faa456235b67a4fdcf8
st.info("⚠️ This is an AI-based prediction and not a medical diagnosis.")