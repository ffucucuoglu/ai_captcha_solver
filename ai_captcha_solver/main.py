# -*- coding: utf-8 -*-
import sys,getopt
import re
from Capture_captcha import capture_captcha
from attacker import coz
from parser import prs_ltrs
from train_model import train

def main():
    help_text="       ┌────────────────────────────────\033[42m MAIN \033[0m────────────────────────────┐\n       │                     ┌───────────┘  └─────────┐                   │\n       v                     v                        v                   v\n\33[101mcapture_captcha\033[0m         \33[101mparse_letters\033[0m            \33[101mtraining\033[0m              \33[101mattack\033[0m\n-l  captcha's url       -p  parse          -t train count    -a  count\n-p  captcha's xpath	                                     -x  captcha's xpath\n-c  count                                                    -l  url\n                                                             -c  captcha's url\n                                                             -w  textbox's xpath\n                                                             -b  button's xpath\n\n\n\n\n\nGithub:\nhttps://github.com/ffucucuoglu/ai_captcha_solver\nBlog:\nhttps://ffucucuoglu.github.io/\n\n"
    argv=sys.argv[1:]
    url="null"
    captcha_url="null"
    a_url="null"
    a_xpath="null"
    xpath="null"
    button_xpath="null"
    textbox_xpath="null"
    uppermosturl="null"
    counter=1
    mode=-3
    try:
        opts,args=getopt.getopt(argv,'ha:f:t:l:px:b:w:c:u:',['xpath=','help=','counter=','url=','attack=','capturecaptcha=','training=','parseletters=','buttonxpath=','textboxxpath=','captchaurl=','uppermosturl='])
    except getopt.GetoptError:
        print('help message')
        sys.exit(2)
        
    for opt,arg in opts:
        
        if opt in('-a','--attack'):
            mode=1
            counter=int(arg)

        elif opt in('-f','--capturecaptcha'):
            mode=-1
            counter=int(arg)
        elif opt in('-t','--training'):
            mode=0
            counter=int(arg)
        elif opt in('-p','--parseletters'):
            mode=-2

    for opt,arg in opts:
        if opt in('-h','--help'):
            print(help_text);sys.exit(2)
        
    for opt,arg in opts:
        if opt in('-l','--url'):
            url=arg

    for opt,arg in opts:
        if opt in('-x','--xpath'):
            xpath=str(arg)
            
    for opt,arg in opts:
        if opt in('-b','--buttonxpath'):
            button_xpath=str(arg)
    for opt,arg in opts:
        if opt in('-w','--textboxxpath'):
            textbox_xpath=str(arg)

    for opt,arg in opts:
        if opt in('-c','--captchaurl'):
            captcha_url=str(arg)
        
    for opt,arg in opts:
        if opt in('-u','--uppermosturl'):
            uppermosturl=str(arg)

            
    if(mode==-3):
        print(help_text)
        sys.exit(2)
    elif(mode==-1):#capturecaptcha
        capture_captcha(counter,url,mode,xpath,uppermosturl)
    elif(mode==0):#training
        train(counter)
    elif(mode==1):#attack
        coz(counter,xpath,url,button_xpath,textbox_xpath,captcha_url)
    elif(mode==-2):#parse letters
        prs_ltrs()
            
if __name__=="__main__":
    main()









