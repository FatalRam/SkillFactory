from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

article = 'AR'
news = 'NW'

POST =[
    (article, 'Статья'),
    (news, 'Новости')
]

class Author(models.Model):
    User_name = models.OneToOneField(User, max_length=50, blank=False, on_delete=models.CASCADE)
    User_rating = models.FloatField(default=0.00)

    def update_rating(self):
        self.User_rating = sum(self.post_rating*3) + sum(self.comment) + sum(self.comment_rating)

class Category(models.Model):
    category_name = models.CharField(max_length=220, unique=True)

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    choice_title = models.CharField(max_length=2, choices=POST)
    create_date = models.DateTimeField(auto_now_add=True)
    category_post = models.ManyToManyField(Category, through='PostCategory')
    heading = models.CharField(max_length=220)
    post_text = models.TextField()
    post_rating = models.FloatField(default=0.00)

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def preview(self):
        return self.post_text[:125, '...']


class PostCategory(models.Model):
    author = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    datetime_comment = models.DateTimeField(auto_now_add=True)
    comment_rating = models.FloatField(default=0.0)

    def like_comment(self):
        self.comment_rating += 1
        self.save()

    def dislike_comment(self):
        self.comment_rating -= 1
        self.save()




