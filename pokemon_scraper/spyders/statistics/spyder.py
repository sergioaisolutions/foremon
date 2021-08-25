from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def statistics_driver(driver, binary):
    return webdriver.Firefox(executable_path = driver, firefox_binary = binary)

def get_url(driver, url):
    return driver.get(url)

def accept_cookies(driver, css_selector_accept_cookies):
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector_accept_cookies))).click()

def pokemon_names(driver, css_selector_to_wait, css_selector_dropdown):

    pokemons_list = list()

    pokemon_selector = driver.find_element_by_css_selector(css_selector_dropdown)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector_to_wait)))
    select_pokemon = Select(pokemon_selector)

    for pokemon in select_pokemon.options:
        pokemons_list.append(pokemon.text)

    return pokemons_list

def pokemon_statistics(driver, css_selector_search_engine, pokemon_names,
                       cp_css_selector, atk_css_selector, def_css_selector):

    search_engine = driver.find_element_by_css_selector(css_selector_search_engine)

    for pokemon_name in pokemon_names:
        search_engine.send_keys(pokemon_name)
        combat_points = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, cp_css_selector)))
        attack = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, atk_css_selector)))
        defense = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, def_css_selector)))
        search_engine.clear()