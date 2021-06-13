from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window() 
driver.get('https://www.thesparksfoundationsingapore.org/')
time.sleep(1)

action = ActionChains(driver) 

two = driver.find_element(By.LINK_TEXT,'2')
two.click()
time.sleep(1)
three = driver.find_element(By.LINK_TEXT,'3')
three.click()
time.sleep(1)
four = driver.find_element(By.LINK_TEXT,'4')
four.click()
time.sleep(1)
five = driver.find_element(By.LINK_TEXT,'5')
five.click()
time.sleep(1)
six = driver.find_element(By.LINK_TEXT,'6')
six.click()
time.sleep(2)

about = driver.find_element(By.LINK_TEXT,'About Us')
about.click()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Vision, Mission and Values").click()
time.sleep(2)
g = driver.find_element(By.LINK_TEXT,"Vision, Mission and Values")
action.move_to_element(g).perform()
time.sleep(2)
a = driver.find_element(By.LINK_TEXT,"Guiding Principles")
action.move_to_element(a).perform()
time.sleep(2)
e = driver.find_element(By.LINK_TEXT,"Advisors and Patrons").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Policies and Code").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Whistle Blowing Policy").click()
time.sleep(2)

driver.find_element(By.LINK_TEXT,"Policies").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Programs").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Workshops").click()
time.sleep(2)

driver.execute_script("window.scrollTo(0, 400)")
time.sleep(2)
window_before = driver.window_handles[0]
driver.find_element(By.CSS_SELECTOR,'a.button-w3layouts.hvr-rectangle-out').click()

window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
driver.execute_script("window.scrollTo(0, 400)")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.find_element_by_id("toTopHover").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"LINKS").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Salient Features").click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Expert Mentor").click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, 700)")
time.sleep(2)
name = driver.find_element_by_name('Name')
name.send_keys('Sarthak Shukla')
time.sleep(2)
passw = driver.find_element_by_name('Email')
passw.send_keys('sarthakshukla@gmail.com')
time.sleep(2)
role = driver.find_element(By.CSS_SELECTOR,"select.form-control")
select = Select(role)
select.select_by_visible_text('Student')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"input.button-w3layouts.hvr-rectangle-out").click()
driver.find_element(By.LINK_TEXT,"Contact Us").click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, 700)")
time.sleep(2)

driver.switch_to.frame(0)
for i in range(4):
    zi = driver.find_element(By.XPATH,'//button[@title = "Zoom in"] ')
    zi.click()
    time.sleep(0.6)
for i in range(4):
    driver.find_element(By.XPATH,'//button[@title = "Zoom out"] ').click()
    time.sleep(0.6)  
driver.switch_to.default_content()    
driver.find_element_by_id("toTopHover").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"a.col-md-6.navbar-brand").click()
    


time.sleep(3)

driver.quit()





