from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import WebDriverException
MAX_WAIT = 10 
class NewVisitorTest(StaticLiveServerTestCase):#(1)
	def setUp(self):#(3)
		self.browser = webdriver.Firefox()
	#def test_can_start_a_list_and_retrive_it_later(self):
	#	self.browser.get(self.live_server_url)
	def tearDown(self):#(3)
		self.browser.quit()
	def wait_for_row_in_list_table(self,row_text):
		start_time = time.time()
		while True:
			try:
				table = self.browser.find_element_by_id('id_list_table')
				rows = table.find_elements_by_tag_name('tr')
				self.assertIn(row_text,[row.text for row in rows])
				return
			except(AssertionError,WebDriverException) as e:
				if time.time() - start_time >MAX_WAIT:
					raise e
				time.sleep(0.5)
	def check_for_row_in_list_table(self,row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text,[row.text for row in rows])
	def test_can_start_a_list_for_one_user(self):#(2)
		#Edith has heard about a cool new online to-do app
		#she goes to check out its homepages
		self.browser.get(self.live_server_url)
		#she notices the page title and header mention to-do lists
		self.assertIn('To-Do',self.browser.title)#(4)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do',header_text)#(5)
		#she is invite to enter a to-do item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)
		#she types "Buy peocock feathers" into a text box(Ediths hobby
		#is tying fly-fishing lures)
		inputbox.send_keys('Buy peacock feathers')
		#when she hits enter,the page updates,and now the page lists
		#"1":Buy peocock feathers" as an item in a to-do list
		inputbox.send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1:Buy peacock feathers')
		#self.assertTrue(
		#	any(row.text == '1:Buy peacock feathers' for row in rows),
		#	f"New to-do item did not appear in table. Contents were:\n{table.text}"
		#)

		#There is still a text box inviting her to add another item.She
		#enters "use peocock feathers to make a fly"(Edith is very methodical)
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		#The page updates again, and now shows both items on her list
		self.wait_for_row_in_list_table('1:Buy peacock feathers')
		self.wait_for_row_in_list_table('2:Use peacock feathers to make a fly')
		#Edith wonders whether the site will  remember her list.
		#Then she sees that the site has generated a unique url for her --
		#There is some explanatory text to the effect

		#she visits that url -her to-do list is still there

		#satisfied ,she goes back to sleep

		#browser.quit()
	def test_multiple_users_can_start_lists_at_different_urls(self):
		#Edith starts a new to-do list
		self.browser.get(self.live_server_url)
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy peacock feathers')
		inputbox.send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1:Buy peacock feathers')
		#she notices a unique url
		edith_list_url = self.browser.current_url
		self.assertRegex(edith_list_url,'/lists/.+')
		#now a new user ,Francis, comes along to the site
		
		##we use a new browser session to make sure that no information
		##of Edith's is coming through from cookies etc
		self.browser.quit()
		self.browser = webdriver.Firefox()
		
		#Francis visits the home page There is no sign of Ediths list
		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers',page_text)
		self.assertNotIn('make a play',page_text)
		#Francis starts a new list by entering a new item he is 
		#less interesting than Edith
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy milk')
		inputbox.send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1:Buy milk')
		#Francis gets his own unique URL
		francis_list_url = self.browser.current_url
		self.assertRegex(francis_list_url,'/lists/.+')
		self.assertNotEqual(francis_list_url,edith_list_url)
		#again there is no trace of Ediths list
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers',page_text)
		self.assertIn('Buy milk',page_text)
		#satisfied they both go sleep
	def test_layout_and_styling(self):
		#Edith goes to the home page 
		self.browser.get(self.live_server_url)
		self.browser.set_window_size(1024,768)
		#she notice the input box is nicely centered
		inputbox = self.browser.find_element_by_id('id_new_item')
		#she starts a new list and sees the input is nicely
		#centered there too
		inputbox.send_keys('testing')
		inputbox.send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1:testing')
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(
			inputbox.location['x']+inputbox.size['width']/2,
			512,
			delta = 10
		)

