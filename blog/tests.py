from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from .models import Post
from .models import *

# Create your tests here.

class BlogTests(TestCase):
    def setUp(self):
        self.user=get_user_model().objects.create(
            username='testuser',
            email='testuser@gmail.com',
            password='secret'
        )

        self.post=Post.objects.create(
            title='test_title',
            body='nice body content',
            author=self.user
        )
    
    def test_string_representation(self):
        post=Post(title="A Sample Test")
        self.assertEquals(str(post),post.title)
    

    def test_post_content(self):
        self.assertEquals(self.post.title,'test_title')
        self.assertEquals(self.post.body,'nice body content')
        #self.assertEquals(self.post.author,'testuser')
    
    def test_post_list(self):
        response=self.client.get(reverse('home'))
        self.assertEquals(response.status_code,200)
        self.assertContains(response,'nice body content')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_post_detail_view(self):
        response=self.client.get('/post/1')
        no_response=self.client.get('/post/2')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(no_response.status_code,404)
        self.assertContains(response, 'test_title')
        self.assertTemplateUsed(response,'post_detail.html')
    
    def test_post_create_view(self):
        response=self.client.post(reverse('post_new'),
        {
            'title':'New title',
            'body':'New body',
            'author':self.user
        })
        print(response)

        self.assertEquals(response.status_code,200)
        self.assertContains(response, 'New title')
        self.assertContains(response,'New body')

    
    def test_post_update_view(self):
        response=self.client.post(reverse('post_edit', args='1'),
        {
            'title':'new updated title',
            'body':'new updated body'
        })

        self.assertEquals(response.status_code,302)

    
    def test_post_delete_view(self):
        response=self.client.post(reverse('post_delete',args='1'))
        self.assertEquals(response.status_code,200)