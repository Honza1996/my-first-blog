from django.db import models


class Pos2(models.Model):
    title = models.CharField(max_length=200)
