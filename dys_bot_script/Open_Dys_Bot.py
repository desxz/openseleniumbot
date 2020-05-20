from selenium import webdriver   #Downlaod driver: https://chromedriver.storage.googleapis.com/80.0.3987.106/chromedriver_win32.zip
import time

def login(personal_user_name,pw):

    URL = "http://sanalsinif.mu.edu.tr/r2r92sy77o1/"               # *Edit* lesson url(don't for history lesson)

    driver = webdriver.Chrome("D:\IE\chromedriver.exe")            # *Edit* chrome driver location
    driver.get("http://dys.mu.edu.tr/")                            

    user_name_login = driver.find_element_by_id("u_name")
    user_name_login.send_keys(personal_user_name)                  # Writing user name
    pass_login = driver.find_element_by_id("pass")
    pass_login.send_keys(pw)                                       # Writing password

    login_button = driver.find_element_by_xpath("/html/body/div/div/div[2]/section/div/div[2]/form[2]/button")
    login_button.click()                                           # Click login button

    driver.get("http://dys.mu.edu.tr/course/view.php?id=22396")    # Enter the course
    driver.find_element_by_partial_link_text("ATB 2802 PRINCIPLES OF KEMAL ATATURK II ŞB: 9910 20192").click()
    driver.find_element_by_id("kati2").click()                     # Login the lesson
    time.sleep(2)                                                  # Wait 2 seconds for any bug
    parent_window = driver.current_window_handle                     # Current browser window
    driver.switch_to.window(parent_window)                           # Switch the windows
    driver.get("chrome://settings/content/siteDetails?site=" + URL)  # Get the site's settings
    section = driver.execute_script("""return document.querySelector("settings-ui").shadowRoot.querySelector("settings-main").shadowRoot.querySelector("settings-basic-page").shadowRoot.querySelector("settings-privacy-page").shadowRoot.querySelector("site-details").shadowRoot.querySelectorAll("site-details-permission")[6].shadowRoot.querySelector("#allow")""")
    section.click()  # Enable adobe flash player
    driver.get(URL)  # Get the site finally
    driver.switch_to.window(driver.window_handles[1])                # For closing pop-up window
    driver.close()

login("mymail@posta.mu.edu.tr", "password")           # *Edit* Enter user mail and password

time.sleep(999999)  # If don't write, browser closing automatically.
