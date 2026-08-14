# weather-forecast
predicting weather
# Weather App

## Description

The Weather App is a Python-based command-line application that retrieves and displays real-time weather information for a specified city using the OpenWeatherMap API.

The application allows users to enter a city name and view important weather details such as temperature, feels-like temperature, humidity, weather condition, wind speed, and country information.

## Features

* Fetches real-time weather data using the OpenWeatherMap API.
* Displays temperature in Celsius.
* Shows the current weather condition.
* Displays humidity and wind speed.
* Provides feels-like temperature.
* Handles invalid city names and API errors.
* Handles connection and timeout errors.
* Provides a simple command-line interface.
* Allows users to search for multiple cities during a single session.

## Technologies Used

* Python
* Requests Library
* OpenWeatherMap API

## Installation

Install the required Python library:

```bash
pip install requests
```

## Configuration

Create an API key from OpenWeatherMap and add it to the application. For security, avoid uploading your API key directly to GitHub. Environment variables can be used to store sensitive credentials.

## Usage

Run the Python program:

```bash
python weather_app.py
```

Enter the name of a city when prompted. The application will retrieve and display the current weather information.

To close the application, enter:

```text
quit
```

## Purpose

This project demonstrates the use of Python for API integration, HTTP requests, JSON data processing, exception handling, and command-line application development.

