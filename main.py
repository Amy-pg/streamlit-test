import streamlit as st
import numpy as np
import pandas as pd

st.title("Streamlit 入門")

st.write("Display Image")

#コメントアウトはctrl+/ね

text_id = st.text_input('楽天ログインＩＤ')
"ログインＩＤ：", text_id

text_pass = st.text_input('楽天ログインパスワード', type="password")
"ログインパス：", text_pass


if st.button('実行'):
    st.write('実行中')
else:
    st.write('実行する場合はボタンを押してください')

