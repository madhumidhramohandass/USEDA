import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np

st.title("🎈 My new app")
st.title('Uber pickups in NYC')
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
DATE_COLUMN = 'date/time'
DATA_URL = ('')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
