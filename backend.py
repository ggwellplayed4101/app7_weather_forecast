import requests

API_KEY="0afce906af37e4d0c3838c4a3355ffb2"

def get_data(place, forecast_days=None):
    url = ("https://api.openweathermap.org/data/2.5/"
           f"forecast?q={place}&appid={API_KEY}")
    response = requests.get(url)
    print (response)
    data =  response.json()
    
    filtered_data = data["list"][:8*forecast_days]

    
    return filtered_data


if __name__ == "__main__": 
    print(get_data(place="Tokyo", forecast_days=3))