import streamlit as st
import plotly.express as px 

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Number of Days to Forecast:", 
                 min_value=1, max_value=5,
                 help="Select how many days you want to forecast")
option = st.selectbox("Select data to view", 
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")


def get_data(days):
    dates = ["2024-01-01", "2024-01-02", "2024-01-03", 
            "2024-01-04", "2024-01-05"]
    temperatures = [10, 12, 15, 11, 9]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures

d, t = get_data(days) 

figure = px.line(x=d, y=t, 
                 labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)