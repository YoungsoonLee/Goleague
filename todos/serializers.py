from rest_framework import serializers
 
from todos.models import Todo
 
class TodoSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Todo
        fields = ('id', 'text', 'due_date', 'done_state')