# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 19:41:19 2023

@author: BOGA SREEVARSHINI
"""

import pandas as pd
import matplotlib.pyplot as plt
import requests

# Define the indicator code and country code
indicator_code = "NY.GDP.MKTP.CD"  # GDP indicator
country_code = "US"  # United States

# Define the World Bank API URL and parameters
base_url = "https://api.worldbank.org/v2/country/{}/indicator/{}?format=json".format(country_code, indicator_code)
params = {
    "date": "2010:2022",
}

# Send a GET request to the World Bank API and get the response
response = requests.get(base_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()[1]

    # Create a DataFrame from the retrieved data
    df = pd.DataFrame(data)
    df.rename(columns={"value": "GDP"}, inplace=True)

    # Drop rows with missing data
    df = df.dropna()

    # Convert the 'date' column to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Create a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(df['date'], df['GDP'], width=250, align='center')
    plt.title("GDP Over Time for {}".format(country_code))
    plt.xlabel("Year")
    plt.ylabel("GDP (in current US dollars)")
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()
else:
    print("Failed to retrieve data from the World Bank API. Status code:", response.status_code)
