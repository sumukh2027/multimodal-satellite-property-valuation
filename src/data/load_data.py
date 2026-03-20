import os
import cv2
import pandas as pd

def load_images(image_path):
    images = []
    image_names = []

    for file in os.listdir(image_path):
        img=cv2.imread(os.path.join(image_path, file))
        if img is not None:
            images.append(img)
            image_names.append(file)

    return images, image_names


def load_targets(csv_path):
    df = pd.read_csv(csv_path)
    return df
