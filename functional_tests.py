from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):#(1)
	def setUp(self):#(3)
		self.browser = webdriver.Firefox()

	def tearDown(self):#(3)
		self.browser.quit()
		
	def test_can_start_a_list_and_retrieve_it_later(self):#(2)
		#Edith has heard about a cool new online to-do app
		#she goes to check out its homepages
		self.browser.get('http://localhost:8000')
		#she notices the page title and header mention to-do lists
		self.assertIn('To-Do',self.browser.title)#(4)
		self.fail('Finish the test')#(5)
		#she is invite to enter a to-do item straight away

		#she types "Buy peocock feathers" into a text box(Ediths hobby
		#is tying fly-fishing lures)

		#when she hits enter,the page updates,and now the page lists
		#"1":Buy peocock feathers" as an item in a to-do list

		#There is still a text box inviting her to add another item.She
		#enters "use peocock feathers to make a fly"(Edith is very methodical)

		#The page updates again, and now shows both items on her list

		#Edith wonders whether the site will  remember her list.
		#Then she sees that the site has generated a unique url for her --
		#There is some explanatory text to the effect

		#she visits that url -her to-do list is still there

		#satisfied ,she goes back to sleep

		#browser.quit()
if __name__ == '__main__':#(6)
	unittest.main(warnings='ignore')#(7)


