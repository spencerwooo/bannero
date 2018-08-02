#!/usr/bin/env python3
# -*- coding=utf-8 -*-


import os
import random
import json
import time


import requests
from bs4 import BeautifulSoup

sdUrl = 'http://simpledesktops.com/browse/'
# sdRandomPage = str(random.randint(1, 49))
sdRandomPage = '16'
sdHeaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'}


def parseHtml():
    sdResponse = requests.get(sdUrl + sdRandomPage, headers=sdHeaders)
    sdHtmlContent = sdResponse.content
    sdSoup = BeautifulSoup(sdHtmlContent, 'html.parser', from_encoding='utf-8')
    sdItems = sdSoup.find_all('img')
    # print(sdItems)
    return sdItems


def getImgUrl(allImgs):
    imgUrl = []
    for eachImg in allImgs:
        sdLinks = eachImg.get('src')
        sdUserUploadLinks = sdLinks.split('.295x184_q100')[0]
        if sdUserUploadLinks.rfind('uploads') != -1:
            imgUrl.append(sdUserUploadLinks)
    # print(imgUrl[0])
    return imgUrl


def getImage():
    sdImgs = parseHtml()
    sdImageUrls = getImgUrl(sdImgs)
    # for eachItem in sdImageUrls:
    #     print(eachItem)
    # randomImage = random.randint(0, len(sdImageUrls) - 1)
    # print(sdImageUrls[randomImage])
    return sdImageUrls


def saveImgToDevice(imgUrl):
    imgData = requests.get(imgUrl).content
    with open('assets/imageToBeUploadedToSmms.png', 'wb') as handler:
        handler.write(imgData)


def uploadToSmms(imgName):
    smUrl = 'https://sm.ms/api/upload'
    smFile = {'smfile': open(imgName, 'rb')}
    smData = {'ssl': True}
    smResponse = requests.post(smUrl, files=smFile, data=smData)
    smRespJson = json.loads(smResponse.content)
    print(smRespJson)
    return smRespJson['data']['url']


def main():
    print("-- Simple Desktop --")
    sdUrl = getImage()
    # imagesLeft = len(sdUrl)
    for eachImgUrl in sdUrl:
        saveImgToDevice(eachImgUrl)
        print("-- An Image From simpledesktops.com Page " + sdRandomPage + " --")
        print("-- Uploading to sm.ms image hosting service --")
        finalImage = uploadToSmms('assets/imageToBeUploadedToSmms.png')
        print(finalImage)
        print("-- Uploaded --")
        with open('simple-desktops.txt', 'a') as sdFile:
            sdFile.write(finalImage + '\n')
        time.sleep(5)
        
    # return finalImage


if __name__ == '__main__':
    main()
