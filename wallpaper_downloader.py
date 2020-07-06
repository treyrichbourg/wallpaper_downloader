#! /usr/bin/env python3
# wallpaper_downloader.py - This program goes to r/wallpapers
# searches a category and downloads the resulting images
# Usage - wallpaper_downloader.py query

import requests, os, praw, sys
from pathlib import Path

# Define variables
reddit = praw.Reddit("wallpaper_downloader", config_interpolation="basic")
subreddit = reddit.subreddit('wallpapers')
#search_query = sys.argv[1]

# Check for directory to store wallpapers, if not there create
# r_wallpapers = Path('r_wallpapers')
# r_wallpapers.mkdir(exist_ok=True)   # Store pictures in ./r_wallpapers
os.makedirs('r_wallpapers', exist_ok=True)

# Let's start by downloading the first 50 results of the search, if there is no search_query entered then we will pull directly from r/wallpapers(hot)
def get_results():
    if len(sys.argv) == 1:
        search_query = subreddit.hot(limit=10)
    elif len(sys.argv) ==2:
        search_query = subreddit.search(sys.argv[1], limit=10)
    search_results = []
    for result in search_query:
        search_results.append(result.url)
    #print(search_results)
    return search_results
# Now we have a list of urls 
# TODO: get a filepath to save each file
def download_wallpapers(test):
    for url in test:
        if url.endswith('.jpg') or url.endswith('.png'):
            res = requests.get(url)
            res.raise_for_status()
            image_file = open(os.path.join('r_wallpapers', os.path.basename(url)), 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()
        else:
            pass

def main():
    test = get_results()
    download_wallpapers(test)
        
        
    #print(test)

    
main()


