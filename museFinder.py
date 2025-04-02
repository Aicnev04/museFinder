from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#User Input
song_name = input("Enter the song name: ")
band_name = input("Enter the band/artist: ")

#Opens Youtube
driver = webdriver.Chrome()
driver.get("https://www.youtube.com")
time.sleep(2)

#Searches for song
youtube_search = driver.find_element("name", "search_query")
youtube_search.send_keys(band_name + " " + song_name)
youtube_search.send_keys(Keys.ENTER)
time.sleep(3)
first_video = driver.find_element("xpath", '(//a[@id="video-title"])[1]')
first_video.click()
time.sleep(3)

#Saves video link
video_link = driver.current_url
time.sleep(1)

#Opens mp3 converter
driver.get("https://ytmp3.nu/CNtD/")
mp3_search = driver.find_element("id", "video")
mp3_search.send_keys(video_link)
mp3_search.send_keys(Keys.ENTER)
time.sleep(25) 

#Downloads mp3 file
download = driver.find_element("xpath", "//button[text()='Download']")
download.click()
time.sleep(2)
driver.quit()
print("Complete")

