from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post
import json

class TestViews(TestCase):

    def test_home_get(self):
        client = Client()
        response = client.get(reverse('blog-home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_about_get(self):
        client = Client()
        response = client.get(reverse('blog-about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/about.html')
    
