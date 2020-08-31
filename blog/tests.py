from django.urls import resolve
from django.test import TestCase
from blog.views import CV_page
from django.urls import reverse

class CVPageTest(TestCase):

    def test_root_url_resolves_to_CV_page_view(self):
        found = resolve('/CV/')
        self.assertEqual(found.func, CV_page)

    def test_CV_uses_correct_template(self):
        response = self.client.get('/CV/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/CV_page.html')

    def test_view_by_def_name(self):
        response = self.client.get(reverse('CV_page'))
        self.assertEqual(response.status_code, 200)
