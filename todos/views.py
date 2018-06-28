from todos.models import Todo
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import filters
 
from todos.serializers import TodoSerializer
 
# GET POST
class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
 
    def perform_create(self, serializer):
        serializer.save()

# Filter
class TodoListFilter(generics.ListAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        """
        This view should return a list of filter Todo.
        """
        done_state = self.request.query_params.get('done_state', None)
        due_date = self.request.query_params.get('due_date', None)

        print(done_state)
        if done_state is not None and due_date is not None:
            return Todo.objects.filter(done_state=done_state, due_date=due_date)
        elif done_state is not None:
            return Todo.objects.filter(done_state=done_state)
        else:
            return Todo.objects.filter(due_date=due_date)
    
# PATCH DELETE
class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer