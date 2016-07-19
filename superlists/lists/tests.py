from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

# Create your tests here.

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		"""
			test if root url resolves to home_page view
			does this by getting the result of resolving '/' and assertEqual
			to home_page (the view from app/lists' views)
		"""
		# resolve: django func to resolve URLs and find what function they map to
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)

		self.assertIn('A new list item', response.content.decode())

		# home.html converted to string
		# now adding context variable to pass to home.html to render then convert

		expected_html = render_to_string(
			'home.html',
			{'new_item_text': 'A new list item'}
		)
		self.assertEqual(response.content.decode(), expected_html)

	def test_home_page_can_save_a_POST_request(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['item_text'] = 'A new list item'

		response = home_page(request)

		self.assertIn('A new list item', response.content.decode())