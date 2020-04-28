from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.views import home_page#(2)
from lists.models import Item
class ItemModelTest(TestCase):
	def test_saving_and_retriveving_item(self):
		first_item = Item()
		first_item.text = 'The first (ever) list item'
		first_item.save()
		
		second_item = Item()
		second_item.text= 'Item the second'
		second_item.save()
		
		save_items = Item.objects.all()
		self.assertEqual(save_items.count(),2)
		
		first_saved_item = save_items[0]
		second_saved_item = save_items[1]
		self.assertEqual(first_saved_item.text,'The first (ever) list item')
		self.assertEqual(second_saved_item.text,'Item the second')
class HomePageTest(TestCase):
# Create your tests here.
	def test_home_page_returns_correct_html(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response,'home.html')
	def test_can_save_a_POST_request(self):
		response = self.client.post('/',data={'item_text':'A new list item'})
		self.assertIn('A new list item',response.content.decode())
		self.assertTemplateUsed(response,'home.html')