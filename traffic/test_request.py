import requests
import json

# The base URL for the DOT Camera dataset (2022-Present)
# This is an example API endpoint from 511ny.org which has data accessible on NYC DOT
def get_cameras():
    key="1"
    format="json"
    API_ENDPOINT = f"https://511ny.org/api/getcameras?key={key}&format={format}"

    # Set up parameters to filter the data (optional)
    # For this example, let's request only 5 records and order by date issued
    params = {
        "$limit": 5,           # Limit to 5 records
        "$order": "dateissued DESC", # Order by date issued, descending (latest first)
        # You could also add filters like: "permittee": "CON EDISON"
    }

    try:
        # 1. Make the GET request
        response = requests.get(API_ENDPOINT, params=params)
        print(response)
        
        # 2. Check for a successful response (status code 200)
        response.raise_for_status() # Raises an HTTPError for bad responses (4xx or 5xx)
        
        # 3. Convert the JSON response text to a Python list of dictionaries
        data = response.json()

        # 4. Print the fetched data
        print(f"Successfully fetched {len(data)} construction permits:")
        
        # Print the first record in a nicely formatted way
        if data:
            print("\n--- First Record ---")
            # Use json.dumps for pretty printing
            print(json.dumps(data[0], indent=4))
        
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")