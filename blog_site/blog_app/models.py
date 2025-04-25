from django.db import models

class Post(models.Model):
  title=models.CharField(max_length=150)
  content=models.CharField(max_length=2000)
  date_posted=models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

# Create your models here.
