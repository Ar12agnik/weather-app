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
def weather(request):
    breif_report=main.get_weather_report(request.GET.get('Location','default'))
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
    params={'last_updated':last_updated,'temp_c':temp_c,'temp_f':temp_f,'condition_text':condition_text,'condition_icon':condition_icon,'wind_mph':wind_mph,'wind_kph':wind_kph,'wind_degree':wind_degree,'wind_dir':wind_dir,'pressure_mb':pressure_mb,'precip_in':precip_in,'humidity':humidity,'feelslike_c':feelslike_c,'uv':uv,}
    return render(request,'weather.html',params)
