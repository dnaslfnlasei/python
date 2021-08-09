from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time

driver = webdriver.Chrome('/Users/youngyoonlim/Developer/python/applecoding/python/python/web crawler/instargram/chromedriver')
driver.get('https://www.8thwall.com/login')

time.sleep(3)
e = driver.find_element_by_css_selector('input[autocomplete="username"]')
e.send_keys('wemad@kkmail.be')
e = driver.find_element_by_css_selector('input[autocomplete="current-password"]')
e.send_keys('Wemad123!')
e.send_keys(Keys.ENTER)
time.sleep(3)

driver.get('https://www.8thwall.com/asdfasdf/artest14/targets')
time.sleep(5)
e = driver.find_element_by_css_selector('#root > div > div.page > main > div > div.button-grid > a:nth-child(1) > img').click()
time.sleep(3)
e = driver.find_element_by_css_selector("input[type='file']").send_keys(r'/Users/youngyoonlim/Developer/python/applecoding/python/python/web crawler/instargram/Test.png')
time.sleep(3)
e = driver.find_element_by_css_selector("body > div.ui.page.modals.dimmer.transition.visible.active > div > div.wizard-actions > div.right > button").click()
time.sleep(3)
e = driver.find_element_by_css_selector("body > div.ui.page.modals.dimmer.transition.visible.active > div > div.wizard-actions > div.right > button").click()
time.sleep(5)
e = driver.find_element_by_css_selector("body > div.ui.page.modals.dimmer.transition.visible.active > div > div > div.editActions-0-2-61 > div > div.moreSpace > div.auto-load-row > label > span").click()
time.sleep(3)
e = driver.find_element_by_css_selector("body > div.ui.page.modals.dimmer.transition.visible.active > div > div > div.previewActions-0-2-65 > div > div > div.right > button").click()
time.sleep(3)
# 크롤링이 끝나면 webdriver 브라우저를 종료한다.
driver.quit()