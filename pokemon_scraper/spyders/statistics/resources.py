# Required and needed files by Selenium.

geckodriver = 'pokemon_scraper\\geckodriver\\geckodriver.exe'
firefox_binary = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'

# Url of the website that we are going to use to extract all the Pokémon data.
# CSS Selector of the "accept cookies" button.

pokemon_url = 'https://pvpoke.com/battle/'
accept_cookies_css_selector = 'button.ncmp__btn:nth-child(2)'

# Needed CSS selectors for gather the required data.

dropdown_last_element_css_selector = '#main > div.section.poke-select-container.single > div:nth-child(1) > select > option:nth-child(1153)'
dropdown_css_selector = 'div.poke:nth-child(1) > select:nth-child(4)'
search_field_css_selector = '#main > div.section.poke-select-container.single > div:nth-child(1) > input'