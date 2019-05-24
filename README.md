# ai_captcha_solver
![Preview](https://raw.githubusercontent.com/ffucucuoglu/ai_captcha_solver/master/img/screenshot1.png)


### Main.py has 4 modes:

#### capture captcha(-f):
This is for download captcha images from link and xpath  
-f + int: Download count(default=1)  
-l + url: captcha's url   
-x + xpath: captcha's xpath  

#### parse letters(-p):  
This is for parsing captcha images.  
-p no argument.  

#### train(-t):  
This is for train deep learning algorithm.  
-t + int: train epochs  

#### attacker(-a):
This is for attack an url.  
-a + int: attack count  
-x + xpath: captcha's xpath  
-l + url: captcha's url    
-c + url: captcha image's url  
-w + xpath: textbox's xpath  
-b + xpath: button's xpath  




## Sample use case:
```
python3 main.py -f 10 -l "https://w3challs.com/challs/Prog/captchas/gen_captcha.php?num=0&" -x "/html/body/img"
```
It will download 10 captchas from link.
```
python3 main.py -p
```
Parse letters in parsedLetters file
```
python3 main.py -t 10
```   
Train and create model_labels.dat,captcha_model.hdf5 files.
```
python3 main.py --url "https://w3challs.com/challs/Prog/captchas/reversecaptcha.php" -a 10 -x "/html/body/img" -b "/html/body/center/form/table/tbody/tr/td/font/center[51]/input" -w "/html/body/center/form/table/tbody/tr/td/font/center[1]/input" -c "https://w3challs.com/challs/Prog/captchas/gen_captcha.php?num=0&"
```
This long command for prediction captcha from url and captcha's xpath then it will submit textbox and press button.
After it will repeat this process for 10 times.


References:[link](https://medium.com/@ageitgey/how-to-break-a-captcha-system-in-15-minutes-with-machine-learning-dbebb035a710)
