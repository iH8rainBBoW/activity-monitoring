from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import LoginForm  # Make sure to replace with the actual import path

class UserLoginTestCase(TestCase):
    def setUp(self):
        self.login_url = reverse('login')  # Make sure to replace with the actual URL

    def test_login_success(self):
        # Create a test user
        user = User.objects.create_user(username='testuser', password='testpassword')

        # Simulate a successful login
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # Expecting a redirect status code
        self.assertRedirects(response, reverse('index'))  # Make sure it redirects to the index page

    def test_login_failure(self):
        # Simulate a login with invalid credentials
        response = self.client.post(self.login_url, {'username': 'invaliduser', 'password': 'invalidpassword'})
        self.assertEqual(response.status_code, 200)  # Expecting a successful response (not a redirect)
        self.assertContains(response, 'Invalid username or password')  # Check if the error message is present in the response

    def test_login_invalid_form(self):
        # Simulate a login with an invalid form (missing required fields)
        response = self.client.post(self.login_url, {})
        self.assertEqual(response.status_code, 200)  # Expecting a successful response (not a redirect)
        self.assertContains(response, 'This field is required')  # Check if the form validation error is present in the response

class UserLogOutTestCase(TestCase):
    def setUp(self):
        self.logout_url = reverse('logout')  # Make sure to replace with the actual URL

    def test_logout(self):
        # Create a test user
        User.objects.create_user(username='testuser', password='testpassword')

        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Simulate a logout
        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect status code
        self.assertRedirects(response, reverse('login_page'))  # Make sure it redirects to the login page
