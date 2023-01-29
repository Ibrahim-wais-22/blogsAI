from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    categories = models.ManyToManyField('Category')
    featured_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    email = models.EmailField()
    website = models.URLField()
    profile_picture = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField()
    approved = models.BooleanField(default=False)
    
    def approve(self):
        self.approved = True
        self.save()
        
    def __str__(self):
        return self.content

class Tag(models.Model):
    name = models.CharField(max_length=255)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.name
