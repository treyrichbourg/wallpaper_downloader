#! /usr/bin/env python3
# wallpaper_downloader.py - This program goes to r/wallpapers
# searches a category and downloads the resulting images

import praw
reddit = praw.Reddit("wallpaper_downloader", config_interpolation="basic")
print(reddit.read_only) # evaluates to true
