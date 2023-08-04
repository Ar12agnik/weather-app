import requests
import json
def get_weather_report(city_name):
    report=requests.get(f'http://api.weatherapi.com/v1/forecast.json?key=d8519cfb1cfb431f956164255232803&q={city_name}&days=1&aqi=yes&alerts=no')
    #print(report.text)
    breif_report=json.loads(report.text)
    return breif_report
'''
last_updated_epoch = breif_report['current']['last_updated_epoch']
last_updated = breif_report['current']['last_updated']
temp_c = breif_report['current']['temp_c']
temp_f = breif_report['current']['temp_f']
is_day = breif_report['current']['is_day']
condition_text = breif_report['current']['condition']['text']
condition_icon = breif_report['current']['condition']['icon']
condition_code = breif_report['current']['condition']['code']
wind_mph = breif_report['current']['wind_mph']
wind_kph = breif_report['current']['wind_kph']
wind_degree = breif_report['current']['wind_degree']
wind_dir = breif_report['current']['wind_dir']
pressure_mb = breif_report['current']['pressure_mb']
pressure_in = breif_report['current']['pressure_in']
precip_mm = breif_report['current']['precip_mm']
precip_in = breif_report['current']['precip_in']
humidity = breif_report['current']['humidity']
cloud = breif_report['current']['cloud']
feelslike_c = breif_report['current']['feelslike_c']
feelslike_f = breif_report['current']['feelslike_f']
vis_km = breif_report['current']['vis_km']
vis_miles = breif_report['current']['vis_miles']
uv = breif_report['current']['uv']
gust_mph = breif_report['current']['gust_mph']
gust_kph = breif_report['current']['gust_kph']

# Printing the values to verify
print("last_updated_epoch:", last_updated_epoch)
print("last_updated:", last_updated)
print("temp_c:", temp_c)
print("temp_f:", temp_f)
print("is_day:", is_day)
print("condition_text:", condition_text)
print("condition_icon:", condition_icon)
print("condition_code:", condition_code)
print("wind_mph:", wind_mph)
print("wind_kph:", wind_kph)
print("wind_degree:", wind_degree)
print("wind_dir:", wind_dir)
print("pressure_mb:", pressure_mb)
print("pressure_in:", pressure_in)
print("precip_mm:", precip_mm)
print("precip_in:", precip_in)
print("humidity:", humidity)
print("cloud:", cloud)
print("feelslike_c:", feelslike_c)
print("feelslike_f:", feelslike_f)
print("vis_km:", vis_km)
print("vis_miles:", vis_miles)
print("uv:", uv)
print("gust_mph:", gust_mph)
print("gust_kph:", gust_kph)'''
if __name__=='__main__':
    breif_report=get_weather_report(input("enter your city name: "))
    last_updated_epoch = breif_report['current']['last_updated_epoch']
    last_updated = breif_report['current']['last_updated']
    temp_c = breif_report['current']['temp_c']
    temp_f = breif_report['current']['temp_f']
    is_day = breif_report['current']['is_day']
    condition_text = breif_report['current']['condition']['text']
    condition_icon = breif_report['current']['condition']['icon']
    condition_code = breif_report['current']['condition']['code']
    wind_mph = breif_report['current']['wind_mph']
    wind_kph = breif_report['current']['wind_kph']
    wind_degree = breif_report['current']['wind_degree']
    wind_dir = breif_report['current']['wind_dir']
    pressure_mb = breif_report['current']['pressure_mb']
    pressure_in = breif_report['current']['pressure_in']
    precip_mm = breif_report['current']['precip_mm']
    precip_in = breif_report['current']['precip_in']
    humidity = breif_report['current']['humidity']
    cloud = breif_report['current']['cloud']
    feelslike_c = breif_report['current']['feelslike_c']
    feelslike_f = breif_report['current']['feelslike_f']
    vis_km = breif_report['current']['vis_km']
    vis_miles = breif_report['current']['vis_miles']
    uv = breif_report['current']['uv']
    gust_mph = breif_report['current']['gust_mph']
    gust_kph = breif_report['current']['gust_kph']

    # Printing the values to verify
    print("last_updated_epoch:", last_updated_epoch)
    print("last_updated:", last_updated)
    print("temp_c:", temp_c)
    print("temp_f:", temp_f)
    print("is_day:", is_day)
    print("condition_text:", condition_text)
    print("condition_icon:", condition_icon)
    print("condition_code:", condition_code)
    print("wind_mph:", wind_mph)
    print("wind_kph:", wind_kph)
    print("wind_degree:", wind_degree)
    print("wind_dir:", wind_dir)
    print("pressure_mb:", pressure_mb)
    print("pressure_in:", pressure_in)
    print("precip_mm:", precip_mm)
    print("precip_in:", precip_in)
    print("humidity:", humidity)
    print("cloud:", cloud)
    print("feelslike_c:", feelslike_c)
    print("feelslike_f:", feelslike_f)
    print("vis_km:", vis_km)
    print("vis_miles:", vis_miles)
    print("uv:", uv)
    print("gust_mph:", gust_mph)
    print("gust_kph:", gust_kph)