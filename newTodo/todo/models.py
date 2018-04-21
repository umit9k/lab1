from django.db import models

class Todo (models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    text = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)


    def __str__(self):
        return self.title