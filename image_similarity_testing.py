import streamlit as st
from compare_images import compare_images

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


def image_similarity_testing(): 
    i = 1
    if st.button("Compare"):
        while i < len(trains) + 1:
            res = compare_images(train1,trains[f"train{i}"])
            con = st.container(border=True)
            col1,col2,col3,col4 = con.columns(4)
            col1.image(train1,width=200)
            col1.text(train1)
            col2.image(trains[f"train{i}"],width=200)
            col2.text(trains[f"train{i}"])
            col3.write(f"Similarity score: {100 - res}")
            i += 1