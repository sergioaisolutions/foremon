from spyder import statistics_driver
from resources import geckodriver, firefox_binary
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

statistics_spyder = statistics_driver(geckodriver, binary = FirefoxBinary(firefox_binary))