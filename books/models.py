from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
import csv
from django.utils.text import slugify


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    description = models.CharField(max_length=2000)
    date = models.DateTimeField(auto_now_add=datetime.now)
    pic = models.ImageField(blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="books"
    )
    category = models.ManyToManyField("Category", blank=True)
    favorite = models.CharField(max_length=200, null=True, blank=True)
    favorited_number = models.IntegerField(default=0)
    favorite_date = models.DateTimeField(null=True, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=200,
        null=True,
        blank=True,
        unique=True,
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Category name={self.name}>"

    def save(self):
        self.slug = slugify(self.name)
        super().save()


class Comment(models.Model):
    text = models.CharField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=datetime.now)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, null=True, related_name="comments"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="comments"
    )


class Suggestion(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    description = models.CharField(max_length=2000)
    date = models.DateTimeField(auto_now_add=datetime.now)
    pic = models.ImageField(blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="suggestions"
    )
    category = models.ManyToManyField("Category", blank=True)
    favorite = models.CharField(max_length=200, null=True, blank=True)
    favorited_number = models.IntegerField(default=0)
    favorite_date = models.DateTimeField(null=True, blank=True)
    accepted = models.BooleanField(default=False)
