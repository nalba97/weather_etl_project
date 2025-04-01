# Weather ETL Project

This project collects weather data from the OpenWeatherMap API and stores it in a PostgreSQL database. The data collection process is automated using Python and runs hourly to keep the database updated with the latest weather information.

## Technologies Used
- Python: For data collection and ETL process
- OpenWeatherMap API: To fetch weather data
- PostgreSQL: To store the collected data
- Python Dotenv: To manage API keys and environment variables

The script fetches the current weather data for Culver City, including temperature and weather description, and inserts it into the PostgreSQL database. The data is collected on an hourly basis to maintain a consistent record of weather changes.

