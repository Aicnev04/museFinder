from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def wait_until_found(driver, by, element):
    try:
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((by, element)))
    except:
        print("Could not download file")
        driver.quit()
        exit(1)

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
print("Opening Youtube")
wait_until_found(driver, By.NAME, "search_query")


#Searches for song
youtube_search = driver.find_element(By.NAME, "search_query")
youtube_search.send_keys(band_name + " " + song_name)
youtube_search.send_keys(Keys.ENTER)

#Browser waits for song to be found
print("Finding Song")
wait_until_found(driver, By.XPATH, '(//a[@id="video-title"])[1]')


#Clicks on first video
first_video = driver.find_element(By.XPATH, '(//a[@id="video-title"])[1]')
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
wait_until_found(driver, By.XPATH, "//button[text()='Download']")


#Downloads mp3 file
download = driver.find_element(By.XPATH, "//button[text()='Download']")
download.click()
print("Downloading song")

#Browser waits for song name
wait_until_found(driver, By.XPATH, "//form/div")

filename = driver.find_element(By.XPATH, "//form/div")
filename = filename.text + ".mp3"
full_path = os.path.join(download_path, filename)
WebDriverWait(driver, 60).until(lambda d: os.path.exists(full_path))
driver.quit()
print("Complete")