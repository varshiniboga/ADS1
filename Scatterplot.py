# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 20:16:53 2023

@author: BOGA SREEVARSHINI
"""

import pandas as pd
import matplotlib.pyplot as plt
import requests

# Define the indicator code for GDP
indicator_code = "NY.GDP.MKTP.CD"

# Define the World Bank API URL and parameters for GDP
base_url = f"https://api.worldbank.org/v2/country/all/indicator/{indicator_code}?format=json"
params = {
    "date": "2010:2022",
}

# Send a GET request to the World Bank API for GDP
response = requests.get(base_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()[1]

    # Create a DataFrame from the retrieved data
    df = pd.DataFrame(data)

    # Filter data for the years 2010 to 2022
    df = df[(df['date'] >= '2010') & (df['date'] <= '2022')]

    # Sort the DataFrame by 'date' in ascending order
    df = df.sort_values(by='date', ascending=True)

    # Create a scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['date'], df['value'], marker='o', alpha=0.7)
    plt.title("Scatter Plot of GDP Over Time (2010-2022)")
    plt.xlabel("Year")
    plt.ylabel("GDP (in current US dollars)")
    plt.grid()
    plt.xticks(rotation=45)
    plt.show()
else:
    print("Failed to retrieve GDP data from the World Bank API. Status code:", response.status_code)
