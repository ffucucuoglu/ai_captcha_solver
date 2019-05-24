from keras.models import load_model
from helpers import resize_to_fit
from imutils import paths
import numpy as np
import imutils
import cv2
import pickle
from selenium import webdriver


MODEL_FILENAME = "captcha_model.hdf5"
MODEL_LABELS_FILENAME = "model_labels.dat"
CAPTCHA_IMAGE_FOLDER = "temp"

def coz(counter,xpath,url,button_xpath,textbox_xpath,captcha_url):
    cdriver=webdriver.Chrome("./chromedriver")
    with open(MODEL_LABELS_FILENAME, "rb") as f:
        lb = pickle.load(f)

    model = load_model(MODEL_FILENAME)#WARNINGS


    for cnt in range(counter):
        cdriver.get(url)
        cdriver.get(str(captcha_url))
        img = cdriver.find_element_by_xpath(str(xpath))
        loc = img.location
        size=img.size
        cdriver.save_screenshot('./notCroppedImages/not_cropped_ss.png')
        croperimg=cv2.imread('./notCroppedImages/not_cropped_ss.png')
        
        cropped_img=croperimg[int(loc['y'])+1:int(loc['y']+size['height']),int(loc['x'])+1:int(loc['x']+size['width'])]

        image = cropped_img
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.copyMakeBorder(image, 20, 20, 20, 20, cv2.BORDER_CONSTANT,value=[255,255,255])#add white border
        thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1] #convert to 1 bit color(white-black)
        
        contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = contours[0]
        letter_image_regions = []
        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour) 
            if w / h > 1.25: #letters width/height
                half_width = int(w / 2)
                letter_image_regions.append((x, y, half_width, h))
                letter_image_regions.append((x + half_width, y, half_width, h))
            else:
                letter_image_regions.append((x, y, w, h))
        letter_image_regions = sorted(letter_image_regions, key=lambda x: x[0])

        predictions = []

        for letter_bounding_box in letter_image_regions:
            x, y, w, h = letter_bounding_box
            letter_image = image[y - 2:y + h + 2, x - 2:x + w + 2]
            letter_image = resize_to_fit(letter_image, 20, 20)#Resize letter 20:20.It must same as training data
            letter_image = np.expand_dims(letter_image, axis=2)
            letter_image = np.expand_dims(letter_image, axis=0)
            prediction = model.predict(letter_image)       
            letter = lb.inverse_transform(prediction)[0]   
            predictions.append(letter)
        captcha_text = "".join(predictions)
        print(format(captcha_text))
        cdriver.get(url)
        textbox=cdriver.find_element_by_xpath(textbox_xpath)
        textbox.clear()
        textbox.send_keys(format(captcha_text))
        button=cdriver.find_element_by_xpath(button_xpath).click()






