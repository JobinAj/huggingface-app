import streamlit as st
import requests

st.title("Hugging Face Model Web Interface")

# User input
text = st.text_area("Enter text to generate:")

if st.button("Generate"):
    response = requests.post("http://backend:8000/generate", json={"text": text})
    if response.status_code == 200:
        st.write("### Generated Output:")
        st.write(response.json()["generated_text"])
    else:
        st.write("Error:", response.text)
