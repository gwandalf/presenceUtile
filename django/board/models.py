from django.db import models

# Create your models here.

class Mission(models.Model):

    title = models.TextField(null=True)
    content = models.TextField(null=True)
    top_point_x = models.IntegerField()
    top_point_y = models.IntegerField()

    def take(self):
        pass
