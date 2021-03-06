import time
# This is to generate a random integer that will represent a url
# index in the links array
from random import randint
# This will allow us to get a random percentage of watch time (i.e. 75%-100%)
# of the video will be viewed
from random import uniform
# Selenium will help us automate opening and controlling browsers
from selenium import webdriver
# This will help us use selenium's .find_element* methods
from selenium.webdriver.common.by import By
# Maybe I will add a feature that searches the video
from selenium.webdriver.common.keys import Keys
# Using pytube to retrieve video duration for YouTube videos
from pytube import YouTube
# This will help us turn the final_views_array into a dictionary that
# summarizes the views per video viewed by the bot
from collections import Counter

# Here the elements of this list each correspond to the browser that will be
# randomly used below. This is done because instantiating webdriver. * opens
# the browser
browsers = ["safari", "firefox", "chrome"]

# An array containing all of the links to my YT music videos so far
links = ["https://www.youtube.com/watch?v=BjEwupErcSU",
"https://www.youtube.com/watch?v=oCp5Enjkc2s",
"https://www.youtube.com/watch?v=-ApgDc9Z6tg",
"https://www.youtube.com/watch?v=hK1DkSVMBbw",
"https://www.youtube.com/watch?v=zyNQJdKfflU"]

daily_views = 3

tally = 0

final_views_array = []

for i in range(daily_views):
    random_driver = browsers[randint(0, len(browsers) - 1)]
    if random_driver == "safari":
        driver = webdriver.Safari()
    elif random_driver == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    random_link = links[randint(0, len(links) - 1)]
    random_watchtime_percentage = uniform(0.1, 0.2)
    if random_driver == "safari":
        driver.get(random_link)
    else:
        driver.get(random_link)
        time.sleep(2)
        large_play_button = driver.find_element(By.CLASS_NAME, "ytp-large-play-button")
        large_play_button.click()
    yt = YouTube(random_link)
    time.sleep(random_watchtime_percentage * yt.length)
    final_views_array.append(yt.title)
    tally += 1
    print('Round ' + str(tally) + " is now complete.")
    driver.quit()

final_viewcount_summary = dict(Counter(final_views_array))

print(final_viewcount_summary)

# This will give us a nicer presentation of the final viewcount summary
for video in sorted(final_viewcount_summary):
    if final_viewcount_summary[video] == 1:
        print("%s was played %s time" % (video, final_viewcount_summary[video]))
    else:
        print("%s was played %s times" % (video, final_viewcount_summary[video]))
