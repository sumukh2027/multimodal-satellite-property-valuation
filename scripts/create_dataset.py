import pandas as pd
import os
from dotenv import load_dotenv
from src.data.data_fetcher import fetch_image

load_dotenv()
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

def create_dataset():
    df = pd.read_csv('data/raw/train.csv')

    image_dir = 'data/raw/images'
    os.makedirs(image_dir, exist_ok=True)

    for i, row in df.iterrows():
        lat, lon, idx = row['lat'], row['long'], row['id']
        save_path = os.path.join(image_dir, f"{idx}.png")

        success = fetch_image(lat, lon, API_KEY, save_path)

        if not success:
            print(f"Failed for id {idx}")


if __name__ == "__main__":
    create_dataset()