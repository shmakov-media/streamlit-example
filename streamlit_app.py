from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests

"""
# Welcome to Streamlit, Сергей Шмаков!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:

Изменения можно вносить прям в гитхабе
"""


profile__sting = st.text_input('Укажите ID-аккаунта')
new_sting = profile__sting[0:8]+'-'+profile__sting[8:12]+'-'+profile__sting[12:16]+'-'+profile__sting[16:20]+'-'+profile__sting[20:32]
####
profile_data = requests.get(f'https://yappy.media/api/profile/{new_sting}').json()
# Данные о профиле
st.write(profile_data['nickname'])
####
data = requests.get(f'https://yappy.media/api/video-list/{new_sting}').json()
st.dataframe(pd.DataFrame(pd.DataFrame(data['data']['results'])))
