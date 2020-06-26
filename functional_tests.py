from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool personal website. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention Sara
        self.assertIn('Sara', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away
        # [...rest of comments as before]

if __name__ == '__main__':
    unittest.main(warnings='ignore')