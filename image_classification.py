import keras
from PIL import Image
from PIL import ImageOps
import cv2
import numpy as np


def machine_classification(img,weights_file ):
    # Load the model
    model = keras.models.load_model(weights_file)

    # Create the array of the right shape to feed into the keras model
    data = np.ndarray(shape=(1, 45, 45, 3), dtype=np.float32)
    image = img
    #image sizing
    size = (45, 45)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    try:
        image=image.save("geeks.jpeg")
	 #turn the image into a numpy array
        img_array=np.array(cv2.imread("geeks.jpeg"))
    except:
        image=image.save("geeks.png")
        img_array=np.array(cv2.imread("geeks.png",cv2.IMREAD_UNCHANGED))    
   
  
        

    
    # Normalize the image
    normalized_image_array = img_array/255 

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    return np.argmax(prediction) # return position of the highest probability