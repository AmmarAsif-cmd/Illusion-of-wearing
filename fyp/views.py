from django.shortcuts import render
from django.shortcuts import redirect
import cv2
import numpy as np
import sys
import logging as log
import datetime as dt
import os

def home(request):
    return render(request,'project/store.html')

def script(request):
   
    
    return render(request,'project/store.html' )

def manual(request):
    return render(request,'project/about.html')

def tst(request ):
    os.system("python fyp/t/Main.py -1 0 -1 1 2")
    return render(request , 'project/store.html')

def shirt(request , num):
    os.system("python fyp/t/Main.py {} -1 -1 4 1".format(num))
    return redirect('/')

def pant(request , num):
    os.system("python fyp/t/Main.py -1 {} -1 1 3".format(num))
    return redirect('/')

def glass(request , num):
    os.system("python fyp/t/Main.py -1 -1 {} 1 1".format(num))
    return redirect('/')

def sleeveless(request , num):
    os.system("python fyp/t/frock.py {} -1 -1 4 1".format(num))
    return redirect('/')

def punjabi(request , num):
    os.system("python fyp/t/ladies_shirt.py {} -1 -1 4 1".format(num))
    return redirect('/')

def printed(request , num):
    os.system("python fyp/t/printed.py {} -1 -1 4 1".format(num))
    return redirect('/')

def didasha(request , num):
    os.system("python fyp/t/didasha.py {} -1 -1 4 1".format(num))
    return redirect('/')

    
# def hair(request , num):
#     os.system("python fyp/t/testing.py -1 -1 0 1 1")
#     return redirect('/')  
