from django.db import models

class IntroductMyself(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=12, blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    def __str__(self):
        return self.name