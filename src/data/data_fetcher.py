import requests
import os

# def fetch_image(lat, lon, api_key, save_path):
#     url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lon}&zoom=18&size=400x400&key={api_key}"
    
#     try:
#         response = requests.get(url)

#         if response.status_code == 200:
#             with open(save_path, 'wb') as f:
#                 f.write(response.content)
#             return True
#     except Exception as e:
#         print("Error:", e)

#     return False

def fetch_image(lat, lon, api_key, save_path):
    url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lon}&zoom=18&size=400x400&maptype=satellite&key={api_key}"
    
    response = requests.get(url)

    print("Status:", response.status_code)   # 👈 ADD THIS

    if response.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(response.content)
        return True
    else:
        print("Error response:", response.text)  # 👈 ADD THIS

    return False