import streamlit as st
import pandas as pd

def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image:url("https://i.imgur.com/wtY58mv.png");
            background-attachment:fixed;
            background-size:cover
            
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_url()
   
st.markdown("<h1 style='font-size:50pt; text-align:center; color:blak;'>Hi Bread</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='font-size:20pt; text-align:center; color:blak;'>너의 위치를 말해봐!</h2>", unsafe_allow_html=True)

title = st.text_input(
    label='',
    placeholder='예시)서울 중구 OO로'
)
