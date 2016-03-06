#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image
import os
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
file_path = input('Please drag the file here...\n')
file_dir, file_full_name = os.path.split(file_path)
file_name = os.path.splitext(file_full_name)[0]
im = Image.open(file_path)
w, h = im.size
new_im = im.convert('L')
with open(os.path.join(file_dir, file_name+'.txt'), 'w') as fout:
	text = ''
	for i in range(h):
		for j in range(w):
			color = new_im.getpixel((j, i))
			text += ascii_char[color//4]
		text += '\n'
	fout.write(text)
