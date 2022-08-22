from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from users.views import register, profile

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)
    
    def test_list_url_is_resolved(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)
    