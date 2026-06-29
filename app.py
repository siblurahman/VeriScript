import streamlit as st

st.set_page_config(
    page_title="VeriScript",
    page_icon="📄",
    layout="wide"
)

st.title("📄 VeriScript")
st.subheader("AI-Powered Document Similarity & Writing Analysis")

st.write("Welcome to VeriScript!")

uploaded_file = st.file_uploader(
    "Upload a document",
    type=["pdf", "docx", "txt"]
)

if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")