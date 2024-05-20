from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class YoutubePlayer:

    def __init__(self, firefox_path, geckodriver_path):
        self.isPlaying, self.isVideoOn = False, False
        self.wasLastOneThumb, self.wasLastOnePalm, self.wasLastOneLeft = False, False, False

        self.binary = FirefoxBinary(firefox_path)
        self.driver = webdriver.Firefox(firefox_binary=self.binary, executable_path=geckodriver_path)
        time.sleep(6)

    def OpenLink(self, link):
        self.driver.get(link)
        self.isVideoOn = True

    def PlayVideo(self):
        if self.wasLastOneThumb == False:
            self.wasLastOneThumb = True
            return

        if self.isPlaying == False and self.isVideoOn:
            try:
                self.driver.find_element(By.CSS_SELECTOR, '.ytp-play-button').click()
            except:
                pass
            self.isPlaying = True

    def PauseVideo(self):
        if self.wasLastOnePalm == False:
            self.wasLastOnePalm = True
            return

        if self.isPlaying == True and self.isVideoOn:
            try:
                self.driver.find_element(By.CSS_SELECTOR, '.ytp-play-button').click()
            except:
                pass
            self.isPlaying = False

    def RewindVideo(self):
        if self.wasLastOneLeft == False:
            self.wasLastOneLeft = True
            return

        if self.isPlaying == True and self.isVideoOn:
            try:
                self.driver.find_elements(By.TAG_NAME, "video")[0].send_keys(Keys.LEFT)
            except:
                pass

    def ResetCounters(self):
        self.wasLastOneThumb, self.wasLastOnePalm, self.wasLastOneLeft = False, False, False
