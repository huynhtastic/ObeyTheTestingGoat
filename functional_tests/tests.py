from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# import unittest

class NewVisitorTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):
		# user opens browser and goes to localhost
		self.browser.get(self.live_server_url)

		# title says "To-Do"
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# enter a to-do item
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		# enters "Buy peacock feathers"
		inputbox.send_keys('Buy peacock feathers')

		# presses enter; page updates and page lists 1: Buy peacock feathers
		inputbox.send_keys(Keys.ENTER)
		edith_list_url = self.browser.current_url
		self.assertRegex(edith_list_url, '/lists/.+')
		self.check_for_row_in_list_table('1: Buy peacock feathers')

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		# self.assertTrue(
		# 	any(row.text == '1: Buy peacock feathers' for row in rows),
		# 	"New to-do item did not appear in table -- its text was:\n%s" % (
		# 		table.text,
		# 	)
		# ) this 6 line test is now converted to the one below:
		self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

		# another textbox to add another item; she puts
		# "Use peacock feathers to make a fly"
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)

		# update page and show both items on list
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		# self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
		# self.assertIn(
		# 	'2: Use peacock feathers to make a fly',
		# 	[row.text for row in rows]
		# ) now converted to:
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

		# unique url for list
		self.fail('Finish the test!')