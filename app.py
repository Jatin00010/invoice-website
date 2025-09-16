!pip install streamlit pyngrok openpyxl

from pyngrok import ngrok

# Start ngrok tunnel
public_url = ngrok.connect(8501)
print("Public URL:", public_url)

# Write streamlit app
with open("app.py", "w") as f:
    f.write('''
import streamlit as st
import pandas as pd
from io import BytesIO

st.title("Invoice to Excel")

# File uploader
uploaded_file = st.file_uploader("Upload Invoice", type=["pdf", "jpg", "png"])

if uploaded_file:
    st.success("File uploaded successfully!")

    if st.button("Send"):
        # Fake processing -> create dummy Excel
        data = {"Field": ["Invoice No", "Amount"], "Value": ["1234", "₹5000"]}
        df = pd.DataFrame(data)

        output = BytesIO()
        df.to_excel(output, index=False, engine="openpyxl")
        st.success("Processing complete!")

        st.download_button("Download Excel", output.getvalue(), "invoice.xlsx")
''')

# Run app
!streamlit run app.py --server.port 8501 --server.headless true
