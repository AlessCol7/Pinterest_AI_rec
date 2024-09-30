from PIL import Image
import numpy as np
import os

def process_images(download_dir):
    processed_images = []
    target_size = (224, 224)

    for img_file in os.listdir(download_dir):
        img_path = os.path.join(download_dir, img_file)
        try:
            with Image.open(img_path) as img:
                img = img.resize(target_size)
                img_array = np.array(img) / 255.0
                processed_images.append(img_array)
        except Exception as e:
            print(f"Error processing {img_file}: {e}")

    return np.array(processed_images)
