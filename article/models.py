# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ArticlePost(models.Model):

    class Meta:
        ordering = ('-created',)


    def __str__(self):
        return self.title

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)

    body = models.TextField()

    created = models.DateTimeField(default=timezone.now)

    updated = models.DateTimeField(auto_created=True, default=timezone.now())



# Create your models here.


# Create your models here.
