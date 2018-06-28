from django.test import TestCase
from .models import Todo
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

# Create your tests here.

# Test Todo model
class ModelTestCase(TestCase):
    """This class defines the test suite for the Todo model."""
    def setUp(self):
        """Define the test client and other test variables."""
        self.todo_text = "GOleague awesome"
        self.todo = Todo(text=self.todo_text)

    def test_model_can_create_a_todo(self):
        """Test the todo model can create a todo."""
        old_count = Todo.objects.count()
        self.todo.save()
        new_count = Todo.objects.count()
        self.assertNotEqual(old_count, new_count)

# Test API
class ViewTestCase(TestCase):
    """Test suite for the api views."""
    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.todo_data = {'text': 'Go Go League~!','due_date': '2019-01-01T00:00:00'}
        self.response = self.client.post('/todos/',self.todo_data,format="json")

    def test_api_can_create_a_todo(self):
        """Test the api has todo creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_todo(self):
        """Test the api can get a given todo."""
        todo = Todo.objects.get()
        response = self.client.get('/todos/'+str(todo.id)+'/', format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, todo)

    def test_api_can_update_todo(self):
        """Test the api can update a given todo."""
        todo = Todo.objects.get()
        change_todo = {'text': 'GO GO NEW'}
        res = self.client.patch('/todos/'+str(todo.id)+'/',change_todo, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_todo(self):
        """Test the api can delete a todo."""
        todo = Todo.objects.get()
        response = self.client.delete('/todos/'+str(todo.id)+'/',format='json',follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)