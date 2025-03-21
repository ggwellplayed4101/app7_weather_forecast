import streamlit as st
import plotly.express as px 
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Number of Days to Forecast:", 
                 min_value=1, max_value=5,
                 help="Select how many days you want to forecast")
option = st.selectbox("Select data to view", 
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        # Get Temperature/ Sky data
        filtered_data = get_data(place, days) 

        if option == "Temperature":
            temperatures = [(dict["main"]["temp"])/10 for dict in filtered_data]  
            dates = [dict["dt_txt"] for dict in filtered_data]

            figure = px.line(x=dates, y=temperatures, 
                            labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            
            images = {"Clear":"images/clear.png",
                    "Clouds":"images/cloud.png",
                    "Rain":"images/rain.png",
                    "Snow":"images/snow.png"}
            
            image_paths = [images[sky] for sky in sky_conditions]
        st.image(image_paths, width=130)
    
    except KeyError:
        st.write("Please enter a valid place!")