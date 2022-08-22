from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from blog.views import about, PostListView, UserPostListView, PostDetailView,  PostCreateView, PostUpdateView, PostDeleteView

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('blog-about')
        self.assertEquals(resolve(url).func, about)

    def test_list_url_is_resolved(self):
        url = reverse('blog-home')
        self.assertEquals(resolve(url).func.view_class, PostListView)

    def test_list_url_is_resolved(self):
        url = reverse('user-posts', args=['some-username'])
        self.assertEquals(resolve(url).func.view_class, UserPostListView)

    def test_list_url_is_resolved(self):
        url = reverse('post-detail', args=[1])
        self.assertEquals(resolve(url).func.view_class, PostDetailView)

    def test_list_url_is_resolved(self):
        url = reverse('post-create')
        self.assertEquals(resolve(url).func.view_class, PostCreateView)

    def test_list_url_is_resolved(self):
        url = reverse('post-update', args=[1])
        self.assertEquals(resolve(url).func.view_class, PostUpdateView)

    def test_list_url_is_resolved(self):
        url = reverse('post-delete', args=[1])
        self.assertEquals(resolve(url).func.view_class, PostDeleteView)