import arrow
import requests

# Get current time
current_time = arrow.now().to('UTC')  # Ensure current time is in UTC

# Define parameters for the current time
params = ','.join([
    'airTemperature', 'airTemperature80m', 'airTemperature100m',
    'airTemperature1000hpa', 'airTemperature800hpa', 'airTemperature500hpa',
    'airTemperature200hpa', 'pressure', 'cloudCover', 'currentDirection',
    'currentSpeed', 'gust', 'humidity', 'iceCover', 'precipitation', 'snowDepth',
    'seaLevel', 'swellDirection', 'swellHeight', 'swellPeriod',
    'secondarySwellPeriod', 'secondarySwellDirection', 'secondarySwellHeight',
    'visibility', 'waterTemperature', 'waveDirection', 'waveHeight',
    'wavePeriod', 'windWaveDirection', 'windWaveHeight', 'windWavePeriod',
    'windDirection', 'windDirection20m', 'windDirection30m', 'windDirection40m',
    'windDirection50m', 'windDirection80m', 'windDirection100m', 'windDirection1000hpa',
    'windDirection800hpa', 'windDirection500hpa', 'windDirection200hpa',
    'windSpeed', 'windSpeed20m', 'windSpeed30m', 'windSpeed40m', 'windSpeed50m',
    'windSpeed80m', 'windSpeed100m', 'windSpeed1000hpa', 'windSpeed800hpa',
    'windSpeed500hpa', 'windSpeed200hpa'
])

response = requests.get(
    'https://api.stormglass.io/v2/weather/point',
    params={
        'lat': 58.7984,
        'lng': 17.8081,
        'params': params,
        'start': current_time.timestamp(),  # Use current time as start
        'end': current_time.timestamp()  # Use current time as end
    },
    headers={
        'Authorization': 'e4ead7ec-6aa1-11ef-9acf-0242ac130004-e4ead85a-6aa1-11ef-9acf-0242ac130004'  # Replace with your actual API key
    }
)

# Check if the request was successful
if response.status_code == 200:
    json_data = response.json()
    print(json_data)
else:
    print(f"Error: {response.status_code}, {response.text}")
