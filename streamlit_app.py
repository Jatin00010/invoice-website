import streamlit as st
import pandas as pd
from io import BytesIO

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="DocStream - Invoice Uploader",
    page_icon="ߓ",
    layout="wide"
)

# --- CUSTOM CSS ---
st.markdown("""
    <style>
        body {
            background-color: black;
            color: white;
        }
        .title {
            font-size: 3rem;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .red {
            color: #e50914;
        }
        .upload-area {
            border: 2px dashed rgba(255,255,255,0.3);
            padding: 40px;
            text-align: center;
            border-radius: 10px;
            transition: all 0.3s ease;
        }
        .upload-area:hover {
            border-color: #e50914;
            background: rgba(229,9,20,0.1);
        }
    </style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown('<div class="title">DOC<span class="red">STREAM</span></div>', unsafe_allow_html=True)
st.write("### Your Documents, Streamed Securely")
st.write("Upload, manage, and extract information from your documents with our AI tools.")

# --- FILE UPLOADER ---
st.markdown('<div class="upload-area">ߓ Drag & Drop Your Invoices Here</div>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload Invoice (PDF, PNG, JPG, JPEG)", type=["pdf", "png", "jpg", "jpeg"])

# --- PROCESSING LOGIC ---
if uploaded_file:
    st.success(f"✅ {uploaded_file.name} uploaded successfully!")

    # Dummy extracted data (replace with AI/OCR later)
    data = {
        "Vendor": ["ABC Pvt Ltd"],
        "Invoice No": ["INV-12345"],
        "Amount": [25000],
        "Date": ["2025-09-16"]
    }
    df = pd.DataFrame(data)

    # Show table
    st.subheader("ߓ Extracted Data")
    st.dataframe(df)

    # Convert to Excel
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Invoice Data")
    buffer.seek(0)

    # Download button
    st.download_button(
        label="⬇️ Download Extracted Data as Excel",
        data=buffer,
        file_name="invoice_data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
