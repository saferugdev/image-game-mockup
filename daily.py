import streamlit as st
from st_click_detector import click_detector
import random
from clock import add_clock
from compare_images import compare

content = """
    <a href='#' id='Image 1'><img width='20%' src='https://replicate.delivery/pbxt/sWeZFZou6v3CPKuoJbqX46ugPaHT1DcsWYx0srPmGrMOCPYIA/out-0.png'></a>
    <a href='#' id='Image 2'><img width='20%' src='https://replicate.delivery/mgxm/8d6a8069-b91f-4e61-8136-fa7c0775532c/out-0.png'></a>
    <a href='#' id='Image 3'><img width='20%' src='https://replicate.delivery/pbxt/sWeZFZou6v3CPKuoJbqX46ugPaHT1DcsWYx0srPmGrMOCPYIA/out-0.png'></a>
    <a href='#' id='Image 4'><img width='20%' src='https://replicate.delivery/mgxm/8d6a8069-b91f-4e61-8136-fa7c0775532c/out-0.png'></a>
    <a href='#' id='Image 5'><img width='20%' src='https://replicate.delivery/pbxt/sWeZFZou6v3CPKuoJbqX46ugPaHT1DcsWYx0srPmGrMOCPYIA/out-0.png'></a>
    <a href='#' id='Image 6'><img width='20%' src='https://replicate.delivery/mgxm/8d6a8069-b91f-4e61-8136-fa7c0775532c/out-0.png'></a>
    <a href='#' id='Image 7'><img width='20%' src='https://replicate.delivery/pbxt/sWeZFZou6v3CPKuoJbqX46ugPaHT1DcsWYx0srPmGrMOCPYIA/out-0.png'></a>
    <a href='#' id='Image 8'><img width='20%' src='https://replicate.delivery/mgxm/8d6a8069-b91f-4e61-8136-fa7c0775532c/out-0.png'></a>
    <a href='#' id='Image 9'><img width='20%' src='https://replicate.delivery/pbxt/sWeZFZou6v3CPKuoJbqX46ugPaHT1DcsWYx0srPmGrMOCPYIA/out-0.png'></a>
    """

images = {
    "Image 1":'https://replicate.delivery/pbxt/sWeZFZou6v3CPKuoJbqX46ugPaHT1DcsWYx0srPmGrMOCPYIA/out-0.png',
    "Image 2":'https://replicate.delivery/mgxm/8d6a8069-b91f-4e61-8136-fa7c0775532c/out-0.png',
    "Image 3":'https://replicate.delivery/pbxt/sWeZFZou6v3CPKuoJbqX46ugPaHT1DcsWYx0srPmGrMOCPYIA/out-0.png',
    "Image 4":'https://replicate.delivery/mgxm/8d6a8069-b91f-4e61-8136-fa7c0775532c/out-0.png',
    "Image 5":'https://replicate.delivery/pbxt/sWeZFZou6v3CPKuoJbqX46ugPaHT1DcsWYx0srPmGrMOCPYIA/out-0.png',
    "Image 6":'https://replicate.delivery/mgxm/8d6a8069-b91f-4e61-8136-fa7c0775532c/out-0.png',
    "Image 7":'https://replicate.delivery/pbxt/sWeZFZou6v3CPKuoJbqX46ugPaHT1DcsWYx0srPmGrMOCPYIA/out-0.png',
    "Image 8":'https://replicate.delivery/mgxm/8d6a8069-b91f-4e61-8136-fa7c0775532c/out-0.png',
    "Image 9":'https://replicate.delivery/pbxt/sWeZFZou6v3CPKuoJbqX46ugPaHT1DcsWYx0srPmGrMOCPYIA/out-0.png',
    }

goal_image = "https://replicate.delivery/mgxm/129d24dc-e39e-4240-8978-88420cc1f910/out-0.png"
black_image = r"images/white.png"
white_image = r"images/black.png"
train1 = r"images/train1.png"
train2 = r"images/train2.png"
train3 = r"images/train3.png"
train4 = r"images/train4.png"
train5 = r"images/train5.png"
train6 = r"images/train6.png"
train7 = r"images/cat.png"
train8 = r"images/train8.png"
train9 = r"images/out-0.png"
train10 = r"images/train10.png"
trains = {
    "train1":train1,
    "train2":train10,
    "train3":train7,
    "train4":train4,
    "train5":train5,
    "train6":train2,
    }


def daily():
    if "selected_img" not in st.session_state:
        st.session_state["selected_img"] = "Image 1"    
    _image = images[st.session_state["selected_img"]]
    st.header("Daily Challenge")
    add_clock()
    i = 1
    if st.button("Compare"):
        while i < len(trains) + 1:
            res = compare(train1,trains[f"train{i}"])
            con = st.container(border=True)
            col1,col2,col3,col4 = con.columns(4)
            col1.image(train1,width=200)
            col1.text(train1)
            col2.image(trains[f"train{i}"],width=200)
            col2.text(trains[f"train{i}"])
            col3.write(f"Similarity score: {100 - res}")
            i += 1
    col1, col2 = st.columns(2)
    with col1:
        st.write("Input")
        st.text_input("Prompt:",value="an astronaut riding a horse on mars, hd, dramatic lighting")
        st.slider("Guidance Scale:",1.0,20.0,7.5)
        st.selectbox("Scheduler:",["K_EULER","DDIM","DPMSolverMultistep","K_EULER_ANCESTRAL","PNDM","KLMS"])
        st.text_input("Negative Prompt:")
        st.button(f"Generate")
        st.text_input("Seed:",disabled=True,value=random.randint(0,100000000))
        st.text_input("Accuracy:",disabled=True,value=random.random()*100)
        st.text_input("Rank:",disabled=True,value=random.randint(1,100))
    with col2:
        st.write("Result")
        tab1, tab2 = st.tabs(["Goal Image", "Current Image"])
        with tab1:
            st.image(goal_image,width=512)
        with tab2:
            st.image(_image,width=512)
        con = st.container(border=True)
        with con:
            st.write("History:")
            clicked = click_detector(content)
            if clicked != "" and clicked != st.session_state["selected_img"]:
                print(f"if clicked is not '': {clicked}")
                st.session_state["selected_img"] = clicked
                st.experimental_rerun()


