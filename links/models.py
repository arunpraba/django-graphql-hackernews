from django.db import models


class Link(models.Model):
    """Links model"""

    url = models.URLField()
    description = models.TextField(blank=True)
