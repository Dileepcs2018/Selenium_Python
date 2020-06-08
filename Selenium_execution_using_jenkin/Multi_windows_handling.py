from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import time
from selenium import webdriver
path ="C:\Dileep\Python_program\Practise\chromedriver.exe"
#from selenium.webdriver import chrome
driver = webdriver.Chrome(executable_path=path)
driver.implicitly_wait(30)
driver.get("https://www.theTestingWorld.com/testings")
driver.find_element_by_xpath("//label[text()= 'Login']").click()
driver.find_element_by_name('_txtUserName').send_keys('test')
driver.find_element_by_name('_txtPassword').send_keys('test')
driver.find_element_by_xpath("//input[@type ='submit' and @value = 'Login']").click()
#driver.find_element_by_link_text('My Account').click()
#or
driver.find_element_by_xpath("//a[contains(text(),'My Account')]").click()
driver.find_element_by_xpath("//a[contains(text(),'Update')]").click()
time.sleep(3)
all_window_handler= driver.window_handles
print(all_window_handler)
mainwin = ""
for win in all_window_handler:
    driver.switch_to.window(win)
    print(driver.current_url)
    if driver.current_url =="https://www.thetestingworld.com/testings/manage_customer.php":
        driver.find_element_by_xpath("//button[text()='Start Download']").click()
        time.sleep(10)
        driver.close()
    elif driver.current_url =="https://www.thetestingworld.com/testings/dashboard.php":
        mainwin=win

driver.switch_to.window(mainwin)
print(driver.current_url)
time.sleep(10)


driver.close()