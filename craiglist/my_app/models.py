from django.db import models

# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField()

    def __str__(self):
        return self.search

    class Meta:
        verbose_name_plural = 'Searches' 