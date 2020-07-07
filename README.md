# wallpaper_downloader
Downloads wallpapers from r/Wallpapers using praw and requests

## Installation 
Download requirements with<br> 
`pip install -r requirements.txt`<br>
<br>
Create an app with reddit and obtain a client id/secret to interact with the API.  Link [here](https://www.reddit.com/prefs/apps/).  The reddit app will require a redirect URI which you can use <kbd>http://localhost:8080</kbd>.  (Note There is no need for username/password as this script accesses the API in read-only mode.)
Create a praw.ini folder and add to cloned repo.  Update `[wallpaper_downloader]` with the information from your reddit app, save the file and now the script will have access to the Reddit API.<br>
```
[DEFAULT]
# A boolean to indicate whether or not to check for package updates.
check_for_updates=True

# Object to kind mappings
comment_kind=t1
message_kind=t4
redditor_kind=t2
submission_kind=t3
subreddit_kind=t5
trophy_kind=t6

# The URL prefix for OAuth-related requests.
oauth_url=https://oauth.reddit.com

# The amount of seconds to ratelimit
ratelimit_seconds=5

# The URL prefix for regular requests.
reddit_url=https://www.reddit.com

# The URL prefix for short URLs.
short_url=https://redd.it

# The timeout for requests to Reddit in number of seconds
timeout=16

[wallpaper_downloader]
client_id= <your_client_id>
client_secret= <your_client_secret>
user_agent= <your_user_agent>
```

## Usage
Navigate to the location of the repository and run this command from your terminal.  If no `search_query` is entered then the script will pull from the r/Wallpapers (hot).  It is set to pull <kbd>.jpeg</kbd> and <kbd>.png</kbd> files from the first 25 posts by default (this can be changed on lines 21 and 23).  Wallpapers will be stored in <kbd>./r_wallpapers</kbd>.<p>
<kbd>python3 wallpaper_downloader.py <search_query_string></kbd>

