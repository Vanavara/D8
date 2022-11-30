from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date



class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Author(models.Model):

   user = models.OneToOneField(User, on_delete=models.CASCADE)
   #user_rate = models.IntegerField(default=0)
   full_name = models.CharField(max_length=255)

class Post(models.Model):

    title = models.CharField(max_length = 255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    category = models.CharField(max_length = 255, default='news')
    dislikes = models.ManyToManyField(Author, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()


    def __str__(self):
        return self.title + ' | ' + str(self.author)


    def get_absolute_url(self):
        return reverse('home')

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

# Create your models here.
