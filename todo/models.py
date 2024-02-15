from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

STATUS_CHOICES = (
  (1, 'Done'),
  (2, 'Doing'),
  (3, 'Undone'),
)

class Todo(models.Model):
  text = models.TextField(validators=[MinLengthValidator(1)], max_length=50)
  date = models.DateTimeField(auto_now=True)
  status = models.IntegerField(choices=STATUS_CHOICES)

  def __str__(self):
    return f"{self.text}"