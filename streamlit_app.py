import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code and a bit of playing around:
"""

num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))



import streamlit as st


import streamlit as st
import requests

# Replace 'YOUR_API_KEY' with your actual Polygon.io API key
POLYGON_API_KEY = 'AKXcSW9xH226RmorFjVWRwlLyJAMseot'

# Streamlit app title
st.title("Polygon.io Data Dashboard")

# Function to fetch data from Polygon.io API
def get_polygon_data(symbol, date):
    base_url = f"https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/day/{date}/{date}"
    params = {"apiKey": POLYGON_API_KEY}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        st.error(f"Error fetching data: {response.text}")
        return None

# Sidebar for user input
symbol = st.sidebar.text_input("Enter Stock Symbol (e.g., AAPL):", "AAPL")
date = st.sidebar.text_input("Enter Date (YYYY-MM-DD):", "2022-01-01")

# Fetch and display data
if st.sidebar.button("Fetch Data"):
    st.subheader(f"Polygon.io Data for {symbol} on {date}")
    data = get_polygon_data(symbol, date)

    if data:
        st.write(data)
