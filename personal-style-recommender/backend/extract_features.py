import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
import pandas as pd
import os

def extract_features(processed_images):
    model = VGG16(weights='imagenet', include_top=False, pooling='avg')
    processed_images = preprocess_input(processed_images)
    features = model.predict(processed_images)
    return features

# Load processed images (ensure you have them)
download_dir = 'data/processed_images'
processed_images = []  # Initialize a list to store processed images

# Load processed images from the directory
for img_file in os.listdir(download_dir):
    img_path = os.path.join(download_dir, img_file)
    if os.path.isfile(img_path):
        img = tf.keras.preprocessing.image.load_img(img_path, target_size=(224, 224))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = img_array / 255.0  # Normalize the image
        processed_images.append(img_array)

# Convert to numpy array
processed_images = np.array(processed_images)

# Example usage
features = extract_features(processed_images)
features_df = pd.DataFrame(features)
features_df.to_csv('data/extracted_features.csv', index=False)
