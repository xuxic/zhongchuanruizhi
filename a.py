# -*- coding: utf-8 -*-
import Image, ImageDraw, ImageFont, ImageColor
import sys
im = Image.open("zhongchuan01.jpg")
draw = ImageDraw.Draw(im)
font = ImageFont.truetype("MSYH.TTC", 30)
draw.text((500,100), "1234", font=font, fill=ImageColor.getrgb("red"))
del draw

# write to stdout
im.save("aaa.png", "PNG")
