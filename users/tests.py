# сделал с ИИ
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterTests(APITestCase):

    def test_register_new_user_success(self):
        """Проверяем успешную регистрацию"""
        url = reverse("auth_register")
        data = {
            "email": "newuser@test.com",
            "password": "strongpass123",
            "username": "testuser",
        }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, 201)
        self.assertIn("email", response.data)
        self.assertNotIn("password", response.data)
        self.assertEqual(User.objects.count(), 1)

        self.assertEqual(response.status_code, 201)

    def test_register_duplicate_email_fails(self):
        """Проверяем, что нельзя зарегаться с существующим email"""
        User.objects.create_user(
            email="existing@test.com",
            password="oldpass123",
            username="olduser",
        )

        url = reverse("auth_register")
        data = {
            "email": "existing@test.com",
            "password": "newpass456",
        }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, 400)
        self.assertIn("email", response.data)
