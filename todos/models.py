from django.db import models
from django.utils import timezone

# Create your models here.
 
class Todo(models.Model):
    """This class represents the todo model."""
    text = models.TextField()
    due_date = models.DateTimeField(default=timezone.now)
    done_state = models.BooleanField(default=False)
    
    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.text)