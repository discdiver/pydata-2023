import requests  # from prefect import flow


# @flow(log_prints=True)
def fetch_weather(lat: float = 40.758896, lon: float = -73.985130):
    base_url = "https://api.open-meteo.com/v1/forecast/"
    weather = requests.get(
        base_url,
        params=dict(latitude=lat, longitude=lon, hourly="temperature_2m"),
    )
    most_recent_temp = float(weather.json()["hourly"]["temperature_2m"][0])
    print(f"Most recent temp C: {most_recent_temp} degrees")
    return most_recent_temp


if __name__ == "__main__":
    fetch_weather()
    # fetch_weather.serve(name="scheduled-deploy", interval="3600")
