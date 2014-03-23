#!/usr/local/bin/python

from PIL import Image, ImageDraw, ImageFont
import random
import sys

font = ImageFont.truetype("Comic Sans MS.ttf", 34, encoding='unic')

im = Image.open('template.jpg')
draw = ImageDraw.Draw(im)

old_positions = []

for arg in sys.argv:
	pos = None
	while pos == None:
		pos = (random.randint(1, im.size[0] - 90), random.randint(1, im.size[1] - 30))
		for (x, y) in old_positions:
			if (pos[0] - x)**2 + (pos[1] - y)**2 < 100**2:
				pos = None
				break
	old_positions.append(pos)
	# color = "hsl(" + str(random.randint(1, 360)) + ", 76%, 45%)"
	color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

	draw.text(pos, arg,  font = font, fill = color)

im.show()

