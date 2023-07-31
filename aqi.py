def calculate_aqi(pm25):
 
    """Calculate the AQI based on PM2.5 concentration"""
    if pm25 <= 12.0:
        aqi = (50 / 12.0) * pm25
    elif pm25 <= 35.4:
        aqi = ((100 - 51) / (35.4 - 12.1)) * (pm25 - 12.1) + 51
    elif pm25 <= 55.4:
        aqi = ((150 - 101) / (55.4 - 35.5)) * (pm25 - 35.5) + 101
    elif pm25 <= 150.4:
        aqi = ((200 - 151) / (150.4 - 55.5)) * (pm25 - 55.5) + 151
    elif pm25 <= 250.4:
        aqi = ((300 - 201) / (250.4 - 150.5)) * (pm25 - 150.5) + 201
    elif pm25 <= 350.4:
        aqi = ((400 - 301) / (350.4 - 250.5)) * (pm25 - 250.5) + 301
    elif pm25 <= 500.4:
        aqi = ((500 - 401) / (500.4 - 350.5)) * (pm25 - 350.5) + 401
    else:
        aqi = -1
    return aqi


def get_health_advisory(aqi):
    if aqi <= 50:
        advisory = "Good, You should try sightseeing while you are here!"
    elif aqi <= 100:
        advisory = "Moderate, Try not to spend too much time here"
    elif aqi <= 150:
        advisory = "Unhealthy for Sensitive Groups, Ensure you have a mask"
    elif aqi <= 200:
        advisory = "Unhealthy, wear a mask while travelling"
    elif aqi <= 300:
        advisory = "Very Unhealthy, try not to go out unless necessary"
    else:
        advisory = "Hazardous, very scary "
    return advisory

cities={'Delhi':78,'Kolkata': 46, 'Mumbai':52,'Manali':5,'Chennai':
22,'Pune':32,'Patna':260}
pm25=0
count=0
c='yes'
while (c!='n'):
    c=input("Enter City else type n for no.")
    if c=="n":
        break
    pm25+=cities[c]
    count+=1
    pmavg=pm25/count

#Example PM2.5 concentration in micrograms per cubic meter (μg/m3)
    
    aqi = calculate_aqi(pmavg)
    advisory = get_health_advisory(aqi)
    print(f"PM2.5 concentration: {pmavg} μg/m3")
    print(f"AQI: {aqi}")
    print(f"Health advisory: {advisory}")