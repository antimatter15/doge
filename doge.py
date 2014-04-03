#!/usr/local/bin/python

from PIL import Image, ImageDraw, ImageFont
import random
import sys
import math

font = ImageFont.truetype("Comic Sans MS.ttf", 34, encoding='unic')

im = Image.open('template3.jpg')
draw = ImageDraw.Draw(im)

old_boxes = []
colors = ['Red', 'Blue', 'Brown', 'Green', 'DarkViolet', 'DarkMagenta', 'Teal']

def rect_dist((ax0, ay0, ax1, ay1), (bx0, by0, bx1, by1)):
	width = max(0, max(ax0, bx0) - min(ax1, bx1))
	height = max(0, max(ay0, by0) - min(ay1, by1))
	return math.sqrt(width**2 + height**2)

gutter = 20

for arg in sys.argv:
	if 'doge.py' in arg:
		continue
	
	box = None
	iterations = 0
	(text_width, text_height) = draw.textsize(arg, font = font)
	while box == None:
		x = random.randint(gutter, im.size[0] - text_width - gutter)
		y = random.randint(gutter, im.size[1] - text_height - gutter)
		box = (x, y, x + text_width, y + text_height)

		iterations += 1
		if iterations > 100:
			break
		for other in old_boxes:
			dist = rect_dist(box, other)
			if dist < 100:
				box = None
				break

	old_boxes.append(box)
	color = random.choice(colors)

	draw.text((box[0], box[1]), arg,  font = font, fill = color)

im.show()
