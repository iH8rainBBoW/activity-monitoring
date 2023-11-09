from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import LoginForm

class UserLoginTestCase(TestCase):
    def setUp(self):
        self.login_url = reverse('login')

    def test_login_success(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

    def test_login_failure(self):
        response = self.client.post(self.login_url, {'username': 'invaliduser', 'password': 'invalidpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid username or password')

    def test_login_invalid_form(self):
        response = self.client.post(self.login_url, {})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required')

class UserLogOutTestCase(TestCase):
    def setUp(self):
        self.logout_url = reverse('logout')

    def test_logout(self):
        User.objects.create_user(username='testuser', password='testpassword')

        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login_page'))
