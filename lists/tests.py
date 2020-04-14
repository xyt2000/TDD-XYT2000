from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.views import home_page#(2)
class HomePageTest(TestCase):
# Create your tests here.
	def test_home_page_returns_correct_html(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response,'home.html')