from django.db import models


class ShortUrlModel(models.Model):
    url = models.URLField()
    code = models.CharField(max_length=5, blank=True, null=False, unique=True)

    def __str__(self):
        return self.url

