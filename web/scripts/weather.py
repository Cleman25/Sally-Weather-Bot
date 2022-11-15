import requests
import json
# TODO: synonym, spellcheck

api_key = "2de35d4c586e85adf3afcbd482bd52dd"
name = input("Please enter your name: ")
with open('../data_location.json', 'r') as infile:
    geo = json.load(infile)
for loc in geo:
    if(loc['name'] == name):
        lat = loc['latitude']
        lon = loc['longitude']
        url = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=metric".format(lat, lon, api_key)
        break

def get_weather():
    response = requests.get(url)
    data = json.loads(response.text)
    # print(data)
    # print("Current Weather: ", data['weather'][0]['description'])
    # print("Maximum Temperature: ", data['main']['temp_min'])
    # print("Minimum Temperature: ", data['main']['temp_max'])
    # print("Humidity", data['main']['humidity'])
    buildStr = f"The current weather  is {data['weather'][0]['description']} with a high of {data['main']['temp_max']} and a low of {data['data'][0]['temp_min']}. The humidity is {data['main'][0]['humidity']}"