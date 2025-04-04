from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

#Directory to send downloaded file
download_path = "C:\\Users\\richi\\OneDrive\\Desktop\\DJ Songs"

#User Input
song_name = input("Enter the song name: ")
band_name = input("Enter the band/artist: ")

#Sets up Chrome
prefs = {"download.default_directory" : download_path}
op = webdriver.ChromeOptions()
op.add_argument("headless")
op.add_argument("--mute-audio")
op.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=op)

#Opens Youtube
driver.get("https://www.youtube.com")

#Browser waits for search bar to be ready
try:
    print("Opening Youtube")
    element = WebDriverWait(driver, 60).until(EC.presence_of_element_located(("name", "search_query"))) 
    print("Youtube Opened")
except:
    print("Could not download file")
    driver.quit()

#Searches for song
youtube_search = driver.find_element("name", "search_query")
youtube_search.send_keys(band_name + " " + song_name)
youtube_search.send_keys(Keys.ENTER)

#Browser waits for song to be found
try:
    print("Finding Song")
    element = WebDriverWait(driver, 60).until(EC.presence_of_element_located(("xpath", '(//a[@id="video-title"])[1]'))) 
except:
    print("Could not download file")
    driver.quit()

#Clicks on first video
first_video = driver.find_element("xpath", '(//a[@id="video-title"])[1]')
first_video.click()
print("Song found")
time.sleep(3)

#Saves video link
video_link = driver.current_url
print("Link extracted")
time.sleep(1)

#Opens mp3 converter
driver.get("https://ytmp3.nu/CNtD/")
mp3_search = driver.find_element("id", "video")
mp3_search.send_keys(video_link)
mp3_search.send_keys(Keys.ENTER)
print("Waiting for song file to process")

#Browser waits for the download button
try:
    element = WebDriverWait(driver, 60).until(EC.presence_of_element_located(("xpath", "//button[text()='Download']"))) 
except:
    print("Could not download file")
    driver.quit()

#Downloads mp3 file
download = driver.find_element("xpath", "//button[text()='Download']")
download.click()
print("Downloading song")

#Browser waits for song name
try:
    element = WebDriverWait(driver, 60).until(EC.presence_of_element_located(("xpath", "//form/div"))) 
except:
    print("Could not download file")
    driver.quit()

filename = driver.find_element("xpath", "//form/div")
filename = filename.text + ".mp3"
full_path = os.path.join(download_path, filename)
WebDriverWait(driver, 60).until(lambda d: os.path.exists(full_path))
driver.quit()
print("Complete")

