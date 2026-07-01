import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="VeriScript",
    page_icon="🛡️",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🛡️ VeriScript")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📄 Verify Document",
        "📊 Reports",
        "⚙️ Settings",
        "ℹ️ About"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("Version v0.1.0-alpha")

# -----------------------------
# Home Page
# -----------------------------
if page == "🏠 Home":

    st.title("🛡️ VeriScript")

    st.caption("Version v0.1.0-alpha")

    st.markdown("## AI-Powered Document Verification Platform")

    st.write(
        """
        Welcome to **VeriScript**.

        Verify certificates, reports, academic documents,
        business files, and official records using Artificial Intelligence.

        Our mission is to make document verification **fast, secure, and trustworthy**.
        """
    )

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📄 Documents Verified", "0")

    with col2:
        st.metric("📑 Reports Generated", "0")

    with col3:
        st.metric("🤖 AI Models", "1")

    with col4:
        st.metric("🟢 System Status", "Online")

    st.divider()

    st.info("🚧 AI Verification Engine is under development.")

# -----------------------------
# Verify Document
# -----------------------------
elif page == "📄 Verify Document":

    st.title("📄 Verify Document")

    st.write("Upload your PDF document below.")

    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=["pdf"]
    )

    if uploaded_file is not None:

        st.success("✅ File uploaded successfully!")

        st.subheader("File Details")

        st.write(f"**Filename:** {uploaded_file.name}")
        st.write(f"**File Size:** {round(uploaded_file.size / 1024, 2)} KB")

        st.divider()

        if st.button("🔍 Verify Document"):

            st.info("🚧 AI Verification module will be added in Version 0.2.")

# -----------------------------
# Reports
# -----------------------------
elif page == "📊 Reports":

    st.title("📊 Reports")

    st.info("Reports feature coming soon.")

# -----------------------------
# Settings
# -----------------------------
elif page == "⚙️ Settings":

    st.title("⚙️ Settings")

    st.info("Settings feature coming soon.")

# -----------------------------
# About
# -----------------------------
elif page == "ℹ️ About":

    st.title("About VeriScript")

    st.write("### Version")
    st.write("v0.1.0-alpha")

    st.write("### Developer")
    st.write("Siblurahman M")

    st.write("### Framework")
    st.write("Python + Streamlit")

    st.write("### Mission")
    st.write(
        "Build an AI-powered document verification platform "
        "that is fast, secure, and reliable."
    )