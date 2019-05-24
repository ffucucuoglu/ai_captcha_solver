import cv2
import pickle
import imutils
import os
import os.path
import numpy as np
from imutils import paths
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.core import Flatten, Dense
from helpers import resize_to_fit


def train(counter):

    LETTER_IMAGES_FOLDER = "parsedLetters"
    MODEL_FILENAME = "captcha_model.hdf5"
    MODEL_LABELS_FILENAME = "model_labels.dat"

    data = []
    labels = []

    folder_count=0
    for _,folders,filee in os.walk('./parsedLetters'):
        folder_count+=len(folders)
    BATCHSIZE=folder_count
    
    for image_file in paths.list_images(LETTER_IMAGES_FOLDER):
        image = cv2.imread(image_file)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        image = resize_to_fit(image, 20, 20)#resize 20:20

        image = np.expand_dims(image, axis=2)
        label = image_file.split(os.path.sep)[-2]

        data.append(image)
        labels.append(label)


    data = np.array(data, dtype="float") / 255.0
    labels = np.array(labels)

    (X_train, X_test, Y_train, Y_test) = train_test_split(data, labels, test_size=0.25, random_state=0)

    lb = LabelBinarizer().fit(Y_train)
    Y_train = lb.transform(Y_train)
    Y_test = lb.transform(Y_test)

    with open(MODEL_LABELS_FILENAME, "wb") as f:
        pickle.dump(lb, f)

    model = Sequential()

    model.add(Conv2D(20, (5, 5), padding="same", input_shape=(20, 20, 1), activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

    model.add(Conv2D(50, (5, 5), padding="same", activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
    
    model.add(Flatten())
    model.add(Dense(500, activation="relu"))

    model.add(Dense(BATCHSIZE, activation="softmax"))

    model.compile(loss="categorical_crossentropy", optimizer="adam",metrics=["accuracy"])
    
    model.fit(X_train, Y_train, validation_data=(X_test, Y_test), batch_size=BATCHSIZE, epochs=counter, verbose=1)
    
    model.save(MODEL_FILENAME)



