import requests
import os

def download_images(image_data, download_dir):
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    for img_data in image_data:
        img_url = img_data['url']
        try:
            response = requests.get(img_url)
            if response.status_code == 200:
                img_name = os.path.join(download_dir, os.path.basename(img_url))
                with open(img_name, 'wb') as img_file:
                    img_file.write(response.content)
                print(f"Downloaded: {img_name}")
            else:
                print(f"Failed to download image: {img_url}")
        except Exception as e:
            print(f"Error downloading {img_url}: {e}")
