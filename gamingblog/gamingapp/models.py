from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField (
        blank = True,
        null = True,
        help_text="Post będzie widoczny na blogu od:"
    )
    def _str_(self):
        return self.title
    