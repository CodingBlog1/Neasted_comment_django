from django.db import models

class Comment(models.Model):
    text = models.CharField(max_length=1000)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return self.text
