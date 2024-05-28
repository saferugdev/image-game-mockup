import streamlit as st
from sidebar import sidebar
from daily import daily
st.set_page_config(layout="wide")

sidebar()

def profile():
    st.session_state["page"] = "profile"

def play_daily_challenge():
    st.session_state["page"] = "daily_challenge"

def play_weekly_challenge():
    st.session_state["page"] = "weekly_challenge"

def main_menu():
    st.session_state["page"] = "main_menu"

if "page" not in st.session_state:
    st.session_state["page"] = "main_menu"
if st.session_state["page"] == "profile":
    st.header("Profile")
    st.button("Back", on_click=main_menu)
    st.text_input("Name")
    my_upload = st.file_uploader("Profile picture", type=["png", "jpg", "jpeg"])
    if my_upload is not None:
        st.image(my_upload,width=150)
elif st.session_state["page"] == "daily_challenge":
    daily()
    st.button("Back", on_click=main_menu)
elif st.session_state["page"] == "weekly_challenge":
    st.header("Weekly Challenge")
    st.button("Back", on_click=main_menu)
elif st.session_state["page"] == "main_menu":
    st.header("Menu")
    st.button("Profile", on_click=profile)
    st.button("Daily Challenge", on_click=play_daily_challenge)
    st.button("Weekly Challenge", on_click=play_weekly_challenge)

