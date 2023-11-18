from django.db import models
from django.contrib.auth.models import User

class UserDetail(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    userimage = models.FileField(null=True)
    aboutyou = models.TextField(null=True)

    def __str__(self):
        return self.usr.username


class Category(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class BlogModel(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=True)
    short = models.TextField(null=True)
    long = models.TextField(null=True)
    image = models.FileField(null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return self.title