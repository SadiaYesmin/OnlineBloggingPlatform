from django.test import TestCase, Client
from django.urls import reverse
from users.models import Profile
import json

class TestViews(TestCase):

    def test_register_post(self):
        client = Client()
        response = client.get(reverse('register'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')
    