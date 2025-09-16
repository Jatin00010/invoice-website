import streamlit as st
import pandas as pd
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import io

# Inject custom CSS
page_bg = """
<style>
.container {
  background: #181c21;
  width: 100%;
  height: 100%;
  margin: 0;
  display: flex;
  align-items: stretch;
  justify-content: stretch;
}

.pattern-bg {
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: repeating-linear-gradient(
    135deg,
    #232526 0px,
    #232526 60px,
    #23252699 70px,
    #414345 130px
  );
}

.cube-svg {
  position: absolute;
  width: 200%;
  height: 200%;
  left: -30%;
  top: -20%;
  background: transparent;
  opacity: 0.7;
  z-index: 1;
  animation: cubeMove 18s linear infinite alternate;
}

@keyframes cubeMove {
  from {
    transform: translateY(0) scale(1);
  }
  to {
    transform: translateY(-20%) scale(1.02) rotate(1deg);
  }
}
</style>

<div class="container">
  <div class="pattern-bg"></div>
</div>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# ---- App content ----
st.title("ߓ Invoice Uploader")
st.write("Upload your invoice and download extracted text as Excel")

uploaded_file = st.file_uploader("Upload Invoice (PDF or Image)", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file:
    st.success("✅ File uploaded successfully!")
    st.write("ߑ Next step: run AI/processing here")
