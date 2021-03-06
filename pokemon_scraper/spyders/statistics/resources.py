# Required and needed files by Selenium.

geckodriver = 'pokemon_scraper\\geckodriver\\geckodriver.exe'
firefox_binary = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'

# Url of the website that we are going to use to extract 
# all the Pokémon data. CSS Selector of the "accept cookies" button.

pokemon_url = 'https://pvpoke.com/battle/'
accept_cookies_css_selector = 'button.ncmp__btn:nth-child(2)'

# Needed CSS selectors for gather the required data.

dropdown_last_element_css_selector = '#main > div.section.poke-select-container.single > div:nth-child(1) > select > option:nth-child(1153)'
search_field_css_selector = '#main > div.section.poke-select-container.single > div:nth-child(1) > input'
dropdown_css_selector = 'div.poke:nth-child(1) > select:nth-child(4)'

combat_points_css_selector = '#main > div.section.poke-select-container.single > div:nth-child(1) > div.poke-stats > h3 > span.stat'
attack_css_selector = '#main > div.section.poke-select-container.single > div:nth-child(1) > div.poke-stats > div.stat-container.attack.clear > div.stat-label > span.stat'
defense_css_selector = '#main > div.section.poke-select-container.single > div:nth-child(1) > div.poke-stats > div.stat-container.defense.clear > div.stat-label > span.stat'
stamina_css_selector = '#main > div.section.poke-select-container.single > div:nth-child(1) > div.poke-stats > div.stat-container.stamina.clear > div.stat-label > span.stat'
overall_css_selector = '#main > div.section.poke-select-container.single > div:nth-child(1) > div.poke-stats > div.stat-container.overall.clear > div > span.stat'
life_css_selector = '#main > div.section.poke-select-container.single > div:nth-child(1) > div.poke-stats > div.hp.bar-back > div.stat'
types_css_selector = '#main > div.section.poke-select-container.single > div:nth-child(1) > div.poke-stats > div.types'