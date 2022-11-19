from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit, Сергей Шмаков!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:

Изменения можно вносить прям в гитхабе
"""


profile = st.text_input('Укажите ID-аккаунта')
data = requests.get(f'https://yappy.media/api/video-list/0af99c31a3714c6f838623ba90527777').json()
st.dataframe(pd.DataFrame(pd.DataFrame(data['data']['results'])))
