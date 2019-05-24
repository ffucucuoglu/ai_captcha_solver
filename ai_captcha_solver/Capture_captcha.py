import cv2
from selenium import webdriver
import sys

def capture_captcha(main_for_counter,url,mode,x_path,uppermosturl):
    if(url=="null"):print("Url is not defined.");sys.exit(2)
    driver = webdriver.Chrome("./chromedriver")
    if(uppermosturl!="null"):
        driver.get(uppermosturl)#uppermost will removed
    for cnt in range(main_for_counter):
        
        driver.get(url)
        img = driver.find_element_by_xpath(x_path)#/html/body/img
        loc = img.location
        size=img.size
        driver.save_screenshot('./notCroppedImages/not_cropped_ss.png')
        croperimg=cv2.imread('./notCroppedImages/not_cropped_ss.png')
        cropped_img=croperimg[int(loc['y'])+1:int(loc['y']+size['height']),int(loc['x'])+1:int(loc['x']+size['width'])]
        cv2.imwrite('./croppedImages/'+str(cnt).zfill(6)+'.png',cropped_img)
    driver.quit()

