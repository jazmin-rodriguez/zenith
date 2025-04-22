import os
import requests

# Load API credentials and URL from environment variables
app_id = os.getenv("EDAMAM_CALC_APP_ID")
app_key = os.getenv("EDAMAM_CALC_APP_KEY")
url = "https://api.edamam.com/api/nutrition-data"



def get_calories_from_edamam(ingredients):
    print("App ID:", app_id)
    print("App Key:", app_key)
    params = {
        'app_id': app_id,
        'app_key': app_key,
        'ingr': ingredients
    }
    try:
        # API request
        response = requests.get(url, params=params)
        response.raise_for_status()  # Will raise an error for HTTP error codes
        
        data = response.json()
        print("API Response Data:", data)  # Output the entire response for debugging

        # Check if calories or other keys are in the response
        if 'calories' in data:
            return data['calories']
        else:
            print("Calories not found in response:", data)
            return "Calories data not found"
    except requests.RequestException as e:
        print("API Request Failed:", e)
        return "Error fetching calorie data"
