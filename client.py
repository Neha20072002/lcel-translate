import requests
import streamlit as st

def translate_text(text, target_language):
    json_body = {
        "input": {
            "language": target_language,
            "text": text
        },
        "config": {},
        "kwargs": {}
    }
    try:
        response = requests.post("https://lecl-translator.onrender.com/chain/invoke", json=json_body)
        response.raise_for_status()  # Ensure the request was successful
        return response.json().get("output", "Translation not found")
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

# Streamlit app configuration
st.set_page_config(page_title="Language Translator", page_icon="🌍", layout="centered")

# Load custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa; /* Light background */
        font-family: 'Arial', sans-serif; /* Clean and modern font */
    }
    .stTitle {
        color: #009900; /* Green for the title */
        font-size: 2.5rem; /* Larger font size for the title */
        text-align: center;
        margin-bottom: 20px;
    }
    .stTextArea textarea {
        border-radius: 10px; /* Rounded corners for text area */
        border: 2px solid #009900; /* Green border */
        padding: 15px;
        font-size: 1rem; /* Adjust font size for readability */
    }
    .stSelectbox select {
        border-radius: 10px; /* Rounded corners for select box */
        border: 2px solid #009900; /* Green border */
        padding: 10px;
        font-size: 1rem; /* Adjust font size for readability */
    }
    .stButton button {
        background-color: #009900; /* Green for button */
        color: white;
        border-radius: 10px; /* Rounded corners for button */
        padding: 12px 25px;
        margin-top: 15px;
        transition: background-color 0.3s ease;
        border: none;
        font-size: 1rem; /* Adjust font size for readability */
    }
    .stButton button:hover {
        background-color: #007700; /* Darker green for hover effect */
    }
    .stWrite {
        font-size: 1.2rem; /* Larger font size for output text */
        color: #333; /* Dark text color for readability */
        text-align: center; /* Center the translated text */
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌍 Language Translator")

text = st.text_area("Enter the text you want to translate", height=150)
target_language = st.selectbox("Select the target language", ["French", "Hindi", "Spanish", "German", "Chinese"])

if st.button("Translate"):
    if text:
        translated_text = translate_text(text, target_language)
        st.markdown(f"<div class='stWrite'>Translated text: <strong>{translated_text}</strong></div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='stWrite'>Please enter some text to translate.</div>", unsafe_allow_html=True)
