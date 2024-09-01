from django.db import models

class Cat(models.Model):
    title = models.CharField('title', max_length=50)
    description = models.TextField('description', max_length=250)
    url = models.URLField('url')
    published_at = models.DateTimeField('date')
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Cat'
        verbose_name_plural = 'Cats'
            