import requests
import pandas as pd


# 1.Extract data
def extract_data_weather(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Has error to fetch data. It is {response.status_code}")

# 2.Transform data
def tranform_data_weather(json_data):
    dataWeather = pd.DataFrame(json_data['current'])

    dataWeather = dataWeather['sunrise','temp','clouds','feels_like']

    return dataWeather
 # 3. Load 
def load_data_csv(data,output_file):
    data.to_csv(output_file,index=False)
    print("Successfully!")

def main(api_url,output_file):
    json_data = extract_data_weather(api_url)
    data =tranform_data_weather(json_data)
    load_data_csv(data,output_file)


if __name__=="__main__":
    api_key = ""  # Thay bằng API Key của bạn
    lat = 10.8231  # Vĩ độ của TP.HCM
    lon = 106.6297  # Kinh độ của TP.HCM
    # URL API
    Url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    output_file ="weather.csv"
    main(Url,output_file)

