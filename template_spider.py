#----------------------Package Imports--------------------------#
import time
import scrapy
from ..items import TemplateSpiderItem
import re
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#---------------------USER INSTRUCTIONS-------------------------#
# 1. Generate Template Spider Using Following Terminal Command:
# Scrapy genspider <name_spider> <website_domain
# 2. Run Spider: scrapy crawl template_spider (name attribute)
# 3. Google Chrome Css Selector Gadget To Help Find Items
# 4. Recall Middelwares and Pipelines Need To Be Activated in Settings
# 5. Databasing in Pipelines.py
# 6. Items in items.py

#------------------Spider Class and Parsing----------------------#
class TemplateSpiderSpider(scrapy.Spider):
    name = 'template_spider'
    allowed_domains = ['https://weather.com/']
    start_urls = ['https://weather.com/weather/monthly/l/fefe88ed9a9980d31378d62d0be14385c1e0b318358e084b0005c7cf39335f51']

    def parse(self, response):
        item             = TemplateSpiderItem()        # Creating Item Data
        css_day          = '.CalendarDateCell--dayCell--3ED7m'
        web_search       = response.css(css_day) # Simple Searches Pulling All a and p
        pattern          = re.compile('\d+°+')    # Temperature Pattern 

        for i in web_search:
            calendar_day         = i.css('span.CalendarDateCell--date--JO3Db::text').get()     
            match                = i.get()                     # Pulling Temperatures      
            match_temps          = pattern.findall(match) #
            item['low_temp']     = min(match_temps)
            item['high_temp']    = max(match_temps)
            item['day_of_month'] = calendar_day
            
            yield item

        def next_month(): # Almost Working 04 Jan 2023... Popup ruins button
            # driver = webdriver.Chrome(executable_path = r'./chromedriver') ## open selenium URL in chrome browser
            driver = webdriver.Chrome(executable_path = r'/Users/alexjimenez/Desktop/Current Desktop/Desktop/Code/CodingCourses/Web Scraping/chromedriver')

            driver.get(TemplateSpiderSpider.start_urls[0])
            right_button = driver.find_element(By.CSS_SELECTOR, '.right')
            right_button.click()
            # driver.switch_to.alert.dismiss()
            print('Right Button Clicked')
            time.sleep(10)
        
            #------INPUT TEXT INTO INPUT BAR-------#
            # inp = driver.find_element(By.CSS_SELECTOR, '#LocationSearch_input')
            # # Sending input text to search field
            # inp.send_keys("Albany, NY")
            # # Pressing enter to search input text
            # inp.send_keys(Keys.ENTER)
            # time.sleep(2)
           
              
        next_month()
           
        
        

        