import streamlit as st

def sidebar():
    with st.sidebar:
        replicate_key = st.text_input(label="Replicate Key:",type="password")
        hf_key = st.text_input(label="HF Key:",type="password")