from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    cat_name = models.CharField(max_length=100)

    def __str__(self):
        return self.cat_name

class Post(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    content = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='image', null=True, blank=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)


    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

