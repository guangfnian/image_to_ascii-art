#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image
import os

#the charactors to draw the ascii art
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

file_path = input('Please drag the file here...\n')
file_dir, file_full_name = os.path.split(file_path)
file_name = os.path.splitext(file_full_name)[0]

im = Image.open(file_path)
w, h = im.size
#the size of new image
W, H = w, h

'''
#to adjust the size of new image
MAX = 80
if W > MAX:
	W, H = MAX, MAX*h//w
if H > MAX:
	H, W = MAX, MAX*w//h
'''

#convert into grayscale
new_im = im.convert('L')
new_im.thumbnail((W, H))

with open(os.path.join(file_dir, file_name+'.txt'), 'w') as fout:
	text = ''
	for i in range(H):
		for j in range(W):
			#get the color of each pixel
			color = new_im.getpixel((j, i))
			text += ascii_char[color//4]
		text += '\n'
	fout.write(text)
