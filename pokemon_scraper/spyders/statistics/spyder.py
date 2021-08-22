from selenium import webdriver

def statistics_driver(driver, binary):
    
    return webdriver.Firefox(executable_path = driver, firefox_binary = binary)