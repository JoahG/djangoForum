from django.db import models

# Create your models here.
class User(models.Model):
	email = models.CharField(max_length=30)
	login = models.CharField(max_length=20)

class Post(models.Model):
	content = models.CharField(max_length=1000)
	created = models.DateTimeField('date published')
	user = models.ForeignKey(User)

class Comment(models.Model):
	content = models.CharField(max_length=500)
	created = models.DateTimeField('date published')
	user = models.ForeignKey(User)
	post = models.ForeignKey(Post)