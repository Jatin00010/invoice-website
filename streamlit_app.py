import streamlit as st

# Inject custom CSS for full background
page_bg = """
<style>
/* Remove Streamlit default background */
[data-testid="stAppViewContainer"] {
    background: #181c21 !important;
}

[data-testid="stHeader"] {
    background: none !important;
}

[data-testid="stToolbar"] {
    right: 2rem;
}

/* Your custom pattern */
.pattern-bg {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  z-index: -1;
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
  z-index: -1;
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

<div class="pattern-bg">
    <div class="cube-svg"></div>
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
