import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

# Load pretrained MobileNetV2 model
model = MobileNetV2(weights='imagenet')

def prepare_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return x

def predict(img_path):
    x = prepare_image(img_path)
    preds = model.predict(x)
    results = decode_predictions(preds, top=3)[0]  # Top 3 predictions
    return [(label, desc, float(prob)) for (label, desc, prob) in results]
