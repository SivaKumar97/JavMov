

import pytesseract
from PIL import Image
import os
import progressbar
from time import sleep
import sys
import io
import json
import base64
from googletrans import Translator
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\shahin-zt381\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# img = Image.open("0_00_01_625__0_00_06_540_0089000000019200108001920.png")
# text = pytesseract.image_to_string(img)
FOLDER_PATH = input("Enter Folder Path Please : ")
FOLDER_PATH =  r'D:\docker\ImageToText\MOVIESUBS' if len(FOLDER_PATH) == 0 else r'D:\docker\Release_x64\TXTImages' if FOLDER_PATH == 'txtpath' else FOLDER_PATH
print(FOLDER_PATH)
def printProgressBar(i,max,fileName):
    n_bar =10 #size of progress bar
    j= i/max
    sys.stdout.write('\r')
    sys.stdout.write(f"[{'=' * int(n_bar * j):{n_bar}s}] {int(100 * j)}% {fileName}")
    sys.stdout.flush()
def getTimeFormat(time):
    time = time.split('_')
    return '0'+time[0]+':'+time[1]+':'+time[2]+','+time[3]
def listDir(dir):
    fileNames = os.listdir(dir)
    FILE_NAME = input("Enter File Name Please : ")
    FILE_NAME = 'MOVSUB.txt' if len(FILE_NAME) == 0 else FILE_NAME
    print(FILE_NAME)
    counter = 1
    textStr = ''
    max = len(fileNames)
    print("Total Files Count : " + str(max))
    # translator = Translator(service_urls=['translate.google.com'])
    for fileName in fileNames:
        timeString = fileName.split('.')[0]
        startTime = timeString.split('__')[0]
        stopTime = timeString.split('__')[1]
        textStr += str(counter) + '\n';
        textStr += getTimeFormat(startTime)
        textStr += ' --> '
        textStr += getTimeFormat(stopTime)
        textStr += '\n'
        img = Image.open(os.path.abspath(os.path.join(dir, fileName)))
        textStr += pytesseract.image_to_string(img, lang='chi_tra')
        # try:
        #     result = translator.translate(cnText, src='zh-cn', dest='en')
        #     if result is not None:
        #         result = json.loads(result.text)
        #         print(result)
        #         textStr += result
        # except Exception as e:
        #     print('Error:', e)
        textStr += '\n'
        printProgressBar(counter,max,fileName)
        counter += 1
    with io.open(FILE_NAME, 'w', encoding='utf-8') as f:
        f.write(textStr)

    print("Completed")



listDir(FOLDER_PATH)

# def listDir(dir):
#     fileNames = os.listdir(dir)
#     FILE_NAME = input("Enter File Name Please : ")
#     FILE_NAME = 'MOVSUB.txt' if len(FILE_NAME) == 0 else FILE_NAME
#     print(FILE_NAME)
#     counter = 1
#     textStr = ''
#     max = len(fileNames)
#     print("Total Files Count : " + str(max))
#     for fileName in fileNames:
#         timeString = fileName.split('.')[0]
#         startTime = timeString.split('__')[0]
#         stopTime = timeString.split('__')[1]
#         textStr += str(counter) + '\n';
#         textStr += getTimeFormat(startTime)
#         textStr += ' --> '
#         textStr += getTimeFormat(stopTime)
#         textStr += '\n'
#         img = Image.open(os.path.abspath(os.path.join(dir, fileName)))
#         textStr += pytesseract.image_to_string(img, lang='chi-sim+eng')
#         textStr += '\n'
#         printProgressBar(counter,max,fileName)
#         counter += 1
#     with open(FILE_NAME, 'w') as f:
#         f.write(textStr)

#     print("Completed")

