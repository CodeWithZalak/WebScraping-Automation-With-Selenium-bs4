from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
import pandas as pd 
import time
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import requests

class IMDBScraper:
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.movie_details = []
    
    def initialize_driver(self):
        service = Service(self.driver_path)
        self.driver = webdriver.Chrome(service=service)
    
    def scrape_movies(self):
        self.driver.get('https://imdb.com')
        time.sleep(2)
        
        # dropdown
        dropdown = self.driver.find_element(By.CLASS_NAME, "ipc-btn__text")
        dropdown.click()
        time.sleep(2)

        # advanced search from dropdown menu
        element = self.driver.find_element(By.LINK_TEXT, 'Advanced Search')
        element.click()
        time.sleep(2)

        # click on advanced title search
        adv_title = self.driver.find_element(By.LINK_TEXT, 'Advanced Title Search')
        adv_title.click()
        time.sleep(2)

        # select feature film
        feature_film = self.driver.find_element(By.ID, 'title_type-1')
        feature_film.click()
        time.sleep(2)

        # select tv movie
        tv_movie = self.driver.find_element(By.ID, 'title_type-2')
        tv_movie.click()
        time.sleep(2)

        # min date
        min_date = self.driver.find_element(By.NAME, 'release_date-min')
        min_date.click()
        min_date.send_keys('1990')
        time.sleep(2)

        # max date
        max_date = self.driver.find_element(By.NAME, 'release_date-max')
        max_date.click()
        max_date.send_keys('2020')
        time.sleep(2)

        # rating min
        rating_min = self.driver.find_element(By.NAME, 'user_rating-min')
        rating_min.click()
        dropdown_2 = Select(rating_min)
        dropdown_2.select_by_visible_text('1.0')
        time.sleep(2)

        # rating max
        rating_max = self.driver.find_element(By.NAME, 'user_rating-max')
        rating_max.click()
        dropdown_3 = Select(rating_max)
        dropdown_3.select_by_visible_text('10')
        time.sleep(2)

        # oscar nominated
        oscar_nominated = self.driver.find_element(By.ID, 'groups-7')
        oscar_nominated.click()
        time.sleep(2)

        # color
        color = self.driver.find_element(By.ID, 'colors-1')
        color.click()
        time.sleep(2)

        # language
        language = self.driver.find_element(By.NAME, 'languages')
        dropdown_4 = Select(language)
        dropdown_4.select_by_visible_text('English')
        time.sleep(2)

        # 250 results
        results_count = self.driver.find_element(By.ID, 'search-count')
        dropdown_5 = Select(results_count)
        dropdown_5.select_by_index(2)
        time.sleep(2)

        # submit
        submit = self.driver.find_element(By.XPATH, '(//button[@type="submit"])[2]')
        submit.click()
        time.sleep(2)

        # current URL
        current_url = self.driver.current_url

        # Get request
        response = requests.get(current_url)

        # Soup object
        soup = BeautifulSoup(response.content, 'html.parser')

        # Result items (starting point)
        list_items = soup.find_all('div', {'class':'lister-item'})

        for item in list_items: 
            movie_title = item.find('h3').find('a').get_text() 
            year = item.find('h3').find('span', {'class':'lister-item-year'}).get_text().replace('(', '').replace(')', '') 
            duration = item.find('span', {'class':'runtime'}).get_text()
            genre = item.find('span', {'class':'genre'}).get_text().strip() 
            rating = item.find('div', {'class':'ratings-imdb-rating'}).get_text().strip() 

            movie_info = {
                'movie_title': movie_title,
                'year': year,
                'duration': duration,
                'genre': genre,
                'rating': rating
            }

            self.movie_details.append(movie_info)

        # Create dataframe
    def to_dataframe(self):    
        df = pd.DataFrame(self.movie_details)
        df.to_csv("IMDB Movies.csv", index=False)
    
    def close(self):
        if self.driver is not None:
            self.driver.quit()


scraper = IMDBScraper(" C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
scraper.initialize_driver()
scraper.scrape_movies()
scraper.to_dataframe()
scraper.close()
