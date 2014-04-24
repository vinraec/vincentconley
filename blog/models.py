from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    category = models.ManyToManyField('blog.Category')

    def __str__(self):
        return '%s' % self.title


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return '%s' % self.title