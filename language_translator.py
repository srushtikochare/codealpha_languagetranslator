import streamlit as st
from deep_translator import GoogleTranslator

# Supported languages
languages = ['english', 'hindi', 'french', 'german', 'spanish', 'japanese', 'chinese', 'arabic']

# Page title
st.set_page_config(page_title="AI Language Translator", layout="centered")
st.title("🌐 Language Translator using AI")

# User input
text = st.text_area("Enter text to translate:")
source_lang = st.selectbox("Select source language:", languages)
target_lang = st.selectbox("Select target language:", languages)

# Translate
if st.button("Translate"):
    if text:
        try:
            translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
            st.subheader("🔄 Translated Text:")
            st.success(translated)
        except Exception as e:
            st.error(f"Translation failed: {e}")
    else:
        st.warning("Please enter text to translate.")
