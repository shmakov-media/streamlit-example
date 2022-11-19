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


#profile = st.text_input('Укажите ID-аккаунта')
data = requests.get(f'https://yappy.media/api/video-list/65e4a7a9-2518-4697-b94a-0992430c036a').json()
st.dataframe(pd.DataFrame(pd.DataFrame(data['data']['results'])))
