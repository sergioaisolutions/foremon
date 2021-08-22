from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def statistics_driver(driver, binary):
    return webdriver.Firefox(executable_path = driver, firefox_binary = binary)

def get_url(driver, url):
    return driver.get(url)

def accept_cookies(driver, css_selector):
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))).click()

def get_pokemon_names(driver, css_selector_to_wait, css_selector_dropdown):

    pokemons_list = list()

    pokemon_selector = driver.find_element_by_css_selector(css_selector_dropdown)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector_to_wait)))
    select_pokemon = Select(pokemon_selector)

    for pokemon in select_pokemon.options:
        pokemons_list.append(pokemon.text)

    return pokemons_list