from django.shortcuts import render
from django.http import HttpResponse
import main
class blah:
    def __init__(self,x) -> None:
        self.hello=x
def index(request):
    x=blah(12)
    params={'blah':x}
    return render(request,'index.html',params)
def avg_temp(start,end):
    sum=0
    for i in range(start,end,):
        sum+=breif_report['forecast']['forecastday'][0]['hour'][i]['temp_c']
    return int(sum/4)


def weather(request):
    global breif_report
    breif_report=main.get_weather_report(request.GET.get('Location','default'))
    avg_4hr_temp=[] 
    start=5
    stop=0
    while stop<=23:
        stop=start+4
        if stop>24:
            stop=24
        avg_4hr_temp.append(avg_temp(start,stop))
        start=stop
    print(avg_4hr_temp)
    last_updated = breif_report['current']['last_updated']
    temp_c = breif_report['current']['temp_c']
    temp_f = breif_report['current']['temp_f']
    condition_text = breif_report['current']['condition']['text']
    condition_icon = breif_report['current']['condition']['icon']
    wind_mph = breif_report['current']['wind_mph']
    wind_kph = breif_report['current']['wind_kph']
    wind_degree = breif_report['current']['wind_degree']
    wind_dir = breif_report['current']['wind_dir']
    pressure_mb = breif_report['current']['pressure_mb']
    precip_in = breif_report['current']['precip_in']
    humidity = breif_report['current']['humidity']
    feelslike_c = breif_report['current']['feelslike_c']
    uv = breif_report['current']['uv']
    precip_mm=breif_report["current"]['precip_mm']
    vis_km=breif_report["current"]['vis_km']
    gust_mph=breif_report["current"]['gust_mph']
    condition=breif_report['forecast']['forecastday'][0]['day']['condition']['text']
    daily_chance_of_rain=breif_report['forecast']['forecastday'][0]['day']['daily_chance_of_rain']
    daily_chance_of_snow=breif_report['forecast']['forecastday'][0]['day']['daily_chance_of_snow']
    #astro
    sunrise=breif_report['forecast']['forecastday'][0]['astro']['sunrise']
    sunset=breif_report['forecast']['forecastday'][0]['astro']['sunset']
    moonrise=breif_report['forecast']['forecastday'][0]['astro']['moonrise']
    moonset=breif_report['forecast']['forecastday'][0]['astro']['moonset']
    moon_phase=breif_report['forecast']['forecastday'][0]['astro']['moon_phase']
    is_moon_up=bool(breif_report['forecast']['forecastday'][0]['astro']['is_moon_up'])
    if is_moon_up:
        is_sun_up='no'
        is_moon_up='yes'
    else:
        is_moon_up='no'
        is_sun_up='yes'
    print(is_sun_up)
    
    params={'last_updated':last_updated,'temp_c':temp_c,'temp_f':temp_f,'condition_text':condition_text,'condition_icon':condition_icon,'wind_mph':wind_mph,'wind_kph':wind_kph,'wind_degree':wind_degree,'sunrise':sunrise,'gust_mph':gust_mph,'condition':condition,'daily_chance_of_snow':daily_chance_of_snow,'daily_chance_of_rain':daily_chance_of_rain,"vis_km":vis_km,'wind_dir':wind_dir,'pressure_mb':pressure_mb,'precip_in':precip_in,'humidity':humidity,'feelslike_c':feelslike_c,'uv':uv,'precip_mm':precip_mm,'5am_8am':avg_4hr_temp[0],'9am_12am':avg_4hr_temp[1],'1pm_4pm':avg_4hr_temp[2],'5pm_8pm':avg_4hr_temp[3],'9pm_12pm':avg_4hr_temp[4],'sunset':sunset,'moonrise':moonrise,'moonset':moonset,'moon_phase':moon_phase,'is_moon_up':is_moon_up,'is_sun_up':is_sun_up}
    return render(request,'weather.html',params)
