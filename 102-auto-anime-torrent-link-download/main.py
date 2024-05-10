import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

show = {}

driver = webdriver.Chrome()

driver.get("https://subsplease.org/")

shows = driver.find_element(By.CSS_SELECTOR, "#menu-item-30 > a")
shows.click()

search_k = driver.find_element(By.CSS_SELECTOR, "#post-wrapper > div > div > div:nth-child(2) > a:nth-child(13)")
search_k.click()

kage_no_link = driver.find_element(By.CSS_SELECTOR, "#post-wrapper > div > div > div.all-shows > div:nth-child(295) > a")
kage_no_link.click()

link_table = driver.find_element(By.CSS_SELECTOR, "#show-release-table")
link_table_tr = link_table.find_elements(By.TAG_NAME, 'tr')
links_torrent = []
nyaa_links = []
for tr in link_table_tr:
    # episode release lable
    show_release_item = tr.find_element(By.CLASS_NAME, "show-release-item")
    label_episode_title = show_release_item.find_element(By.CLASS_NAME, "episode-title")
    label_episode_title.click()
    
    # time.sleep(2)
    
    # now download link are visible
    download_links = show_release_item.find_element(By.CLASS_NAME, "download-links")
    links = download_links.find_elements(By.TAG_NAME, 'a')
    
    for link in links:
        span = link.find_element(By.TAG_NAME, 'span')
        if span.text == 'Torrent':
            links_torrent.append(link)
        # link.get_attribute("href")
    
    
    link = links_torrent[-1]
    nyaa_links.append(link.get_attribute("href"))
    
    links_torrent.clear()
        
    
    
    # episode release time
    # release_item_time = tr.find_element(By.CLASS_NAME, "release-item-time")
    
for l in nyaa_links:
    driver.get(l)

driver.close()