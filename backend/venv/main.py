import requests

# Replace with your Bearer token
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAADvwzgEAAAAA4bZNzV1XT%2FSzFipxLeiotQndDj4%3DhRcfCiVWCvnNIWkKFKQvlnWxzotmCBPmMoMjXgkl5yzZaKp8eI"

# Set up headers with Bearer token for authentication
headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

# Endpoint to get authorized user details (v1.1)
url = "https://api.twitter.com/1.1/account/verify_credentials.json"

# Make a GET request
response = requests.get(url, headers=headers)

# Check for successful response
if response.status_code == 200:
    user = response.json()
    print("Username:", user["screen_name"])
    print("Name:", user["name"])
    print("ID:", user["id"])
    print("Bio:", user["description"])
    print("Location:", user["location"])
    print("Followers:", user["followers_count"])
    print("Following:", user["friends_count"])
    print("Profile Image URL:", user["profile_image_url_https"])
else:
    print(f"Error: {response.status_code} - {response.text}")
