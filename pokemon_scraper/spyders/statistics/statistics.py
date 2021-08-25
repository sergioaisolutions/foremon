from spyder import *
from resources import *
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

statistics_spyder = statistics_driver(geckodriver, binary = FirefoxBinary(firefox_binary))

get_url(statistics_spyder, pokemon_url)
accept_cookies(statistics_spyder, accept_cookies_css_selector)
pokemon_names = pokemon_names(statistics_spyder, dropdown_last_element_css_selector, dropdown_css_selector)

pokemon_statistics(statistics_spyder, search_field_css_selector, pokemon_names,
                   combat_points_css_selector, attack_css_selector, defense_css_selector)