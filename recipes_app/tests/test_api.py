from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from recipes_app.models import Recipe
from rest_framework.authtoken.models import Token



class RecipeAPITestCaseHappy(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.recipe = Recipe.objects.create()

    def test_get_recipe(self):
        url = reverse('recipe-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_recipe_authenticated(self):
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_recipe_detail_authenticated(self):
        url = reverse('recipe-detail', kwargs={'pk': self.recipe.id})


class RecipeAPITestCaseUnhappy(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_list_post_recipe(self):
        url = reverse('recipe-list')
        data = {'title': 'Pizza',
                'description': 'Tunfisch Pizza',
                'author': self.user.id
                }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)