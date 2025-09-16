import streamlit as st
import pandas as pd
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import io

# ߎ App Title
st.title("ߓ Invoice Text Extractor")

# File uploader (PDF or Image)
uploaded_file = st.file_uploader(
    "Upload Invoice (PDF or Image)", 
    type=["pdf", "png", "jpg", "jpeg"]
)

if uploaded_file:
    st.success("✅ File uploaded successfully!")

    text = ""

    # If PDF → convert to image first
    if uploaded_file.type == "application/pdf":
        pdf_bytes = uploaded_file.read()
        images = convert_from_path(io.BytesIO(pdf_bytes))
        for img in images:
            text += pytesseract.image_to_string(img)
    else:
        # Image file
        image = Image.open(uploaded_file)
        text = pytesseract.image_to_string(image)

    # Show extracted text
    st.subheader("ߓ Extracted Text:")
    st.text_area("Text", text, height=200)

    # Convert text → Excel
    if text.strip():
        df = pd.DataFrame({"Extracted Text": [text]})
        excel_buffer = io.BytesIO()
        with pd.ExcelWriter(excel_buffer, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="Invoice")

        st.download_button(
            label="⬇️ Download Excel",
            data=excel_buffer.getvalue(),
            file_name="invoice_output.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
