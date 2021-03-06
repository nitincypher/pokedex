# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import pickle
import cv2
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
	help="path to trained model model")
ap.add_argument("-l", "--labelbin", required=True,
	help="path to label binarizer")
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())
# Three parameters when called are:
    # 1. --model: path to trained model
    # 2. --labelbin: path to label binarizer file
    # 3. --image: input image path
    
# load the image
image = cv2.imread(args["image"])
output = image.copy()
 
# pre-process the image in the exact same manner as training
image = cv2.resize(image, (96, 96))
image = image.astype("float") / 255.0
image = img_to_array(image)
image = np.expand_dims(image, axis=0)

# load the trained convolutional neural network and the label binarizer
print("[INFO] loading network...")
model = load_model(args["model"])
lb = pickle.loads(open(args["labelbin"], "rb").read())
 
# classify the input image
print("[INFO] classifying image...")
proba = model.predict(image)[0]
idx = np.argmax(proba)
label = lb.classes_[idx]
print(lb)
print(idx)  
print(label)

# if input file name contains correct class, marked as correct
#filename = args["image"][args["image"].rfind(os.path.sep) + 1:]
#correct = "correct" if filename.rfind(label) != -1 else "incorrect"
 
text_file = open("../labels.txt", "r")
lines = text_file.readlines()

i = 0
for pokemon in lines:
    if i==idx:
        correct = pokemon.strip().split("/")[-1]
    i=i+1
# build the label and draw the label on the image
label = "{}: {:.2f}%".format(correct, proba[idx] * 100)
output = imutils.resize(output, width=400)
cv2.putText(output, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
	0.7, (0, 255, 0), 2)
 
# show the output image
print("[INFO] {}".format(label))
cv2.imshow("Output", output)
cv2.waitKey(0)

# Terminal Command to run on an example:
# python classify.py --model <MODEL_NAME>.model --labelbin lb.pickle --image examples/<FILE_NAME.jpg>
# image exits on the press of a key