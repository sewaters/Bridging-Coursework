from django.http import HttpRequest
from django.urls import resolve
from django.test import TestCase
from blog.views import CV_page

class CVPageTest(TestCase):

    def test_root_url_resolves_to_CV_page_view(self):
        found = resolve('/CV/')
        self.assertEqual(found.func, CV_page)

    def test_CV_page_returns_correct_html(self):
        request = HttpRequest()
        response = CV_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.strip().startswith('<html>'))
        self.assertIn('<title>Sara Waters</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

    def test_uses_CV_template(self):
        response = self.client.get('/CV/')
        self.assertTemplateUsed(response, 'blog/CV_page.html')