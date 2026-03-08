from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(default=0)  # optional: 0-100%

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True)
    skills = models.ManyToManyField(Skill, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Add this field to store project images
    image = models.ImageField(upload_to='projects/', blank=True, null=True)

    def __str__(self):
        return self.title