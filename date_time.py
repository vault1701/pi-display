#!/usr/bin/env python3

from datetime import datetime
import logging
import locale

from PIL import Image, ImageDraw

import constants as const
import util

# creates the date_time 'module' that can be pasted to the main image
def create_module(config):
    module = Image.new("1", (const.SCREEN_W, const.SCREEN_H), 1)
    draw = ImageDraw.Draw(module)
    
    now = datetime.now()
    time = now.strftime("%H:%M")
    date = now.strftime("%B %d")
    
    locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')
    
    #halfh = const.SCREEN_H/2
    #halfw = const.SCREEN_W/2
    
    # guidelines for drawing in the center
    #draw.line([(0, const.SCREEN_H/2), (const.SCREEN_W, const.SCREEN_H/2)], fill="black", width=1)
    #draw.line([(halfw, 0), (halfw, const.SCREEN_H)], fill="black", width=1)

    # time
    draw.text(
        xy=(62, 60),
        text="{}".format(time),
        font=util.load_font(270),
    )

    # date
    draw.text(
        xy=(50, 340),
        text="{}".format(now.strftime("%A, %B %d")),
        font=util.load_font(64),
    )

    return module