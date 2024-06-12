import os
# set TF_ENABLE_ONEDNN to 0
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from tensorflow.keras.models import load_model # TensorFlow is required for this example
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg19 import preprocess_input
import numpy as np


def load_custom_model():
    global model
    model = load_model('best_model.h5')

    # print(">> model loaded")




def predict(image_path):
    # print('inside the predict func: ', type(model))
    img = image.load_img(image_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = preprocess_input(x)
    x = np.expand_dims(x, axis=0)

    preds = model.predict(x)

    # print the class labels for the predictions
    labels = ['Ai', 'Real']

    # print the predictions
    return labels[np.argmax(preds)]
