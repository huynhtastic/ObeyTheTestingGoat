from django.core.urlresolvers import resolve
from django.test import TestCase
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