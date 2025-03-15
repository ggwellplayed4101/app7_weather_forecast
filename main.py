import streamlit as st

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Number of Days to Forecast:", 
                 min_value=1, max_value=5,
                 help="Select how many days you want to forecast")
option = st.selectbox("Select data to view", 
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")