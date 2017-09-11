# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class ImageData(models.Model):
    id = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=2000)

    def __str__(self):
        return  self.url