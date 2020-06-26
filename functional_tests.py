from selenium import webdriver

browser = webdriver.Firefox(executable_path=r'/Users/sarawaters/Documents/University/2nd Year/BCoursework/geckodriver')
browser.get('http://localhost:8000')

assert 'Django' in browser.title