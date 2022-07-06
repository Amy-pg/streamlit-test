from turtle import st
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

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


# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1,11))
# )

# st.write(option)

# if st.checkbox("Show Image"):
#     img = Image.open("greenimage.png")
#     st.image(img, use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69, 139.70],
#     columns=['lat','lon']
# )
# st.map(df)

# '''

# # 見出し１
# ## 見出し２
# ### 見出し３

# '''