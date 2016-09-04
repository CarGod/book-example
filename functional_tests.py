# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)


    def tearDown(self):
        self.browser.quit()


    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith hearda cool online application todo.
        # She looked at the project home page.
        self.browser.get("http://localhost:8000")

        # She noted that the title of the page and head include "To-Do" word
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Applications invited her to enter a todo
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She entered the "Buy peacock feathers" in the text box
        # Edith is interested in is the use of fly-fishing for bait
        inputbox.send_keys('Buy peacock feathers')

        # She pressed the Enter key, the page updated.
        # Todo table show "1: Buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # Page and displays a text box, you can enter additional todi.
        # She entered the "Use peacock feathers to make a fly"
        # Edith things very organized
        self.fail('Finish the test!')

        # Page updated again, her list shows the two todo.
        # [...]
if __name__ == '__main__':
    unittest.main(warnings='ignore')