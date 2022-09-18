from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Books(models.Model):
    book_name=models.CharField(max_length=120)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        self.book_name