import unittest
from django.test import LiveServerTestCase
from selenium import webdriver


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_read_through_cv_page(self):
        # Emma has heard about a cool personal website. She goes
        # to check out its homepage
        self.browser.get(self.live_server_url)

        # She notices the page title says her name and header mention a CV
        self.assertIn('Sara', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Sara', header_text)
        nav_text = self.browser.find_element_by_id("CV").text
        self.assertIn('CV', nav_text)
        self.browser.find_element_by_id("CV").click()

        self.browser.get("http://127.0.0.1:8000/CV/")
        # She reads through each section of text on the page
        title_text = self.browser.find_element_by_id("Title").text
        self.assertIn('CV', title_text)
        text = self.browser.find_element_by_id('CV Texts')
        self.assertIsNotNone(text)

        #She notices there are links to Sara's accounts on linked In and GitHub and tries them
        actual_url = self.browser.find_element_by_id('LinkedIn').get_attribute('href')
        self.assertEqual(actual_url, 'https://www.linkedin.com/in/sara-waters-856393173/')
        actual_url = self.browser.find_element_by_id('GitHub').get_attribute('href')
        self.assertEqual(actual_url, 'https://github.com/sewaters')



if __name__ == '__main__':
    unittest.main(warnings='ignore')