from django.db import models

# Create your models here.


class Mission(models.Model):

    title = models.TextField(null=True)
    content = models.TextField(null=True)

    def __str__(self):
        """
        :return:title
        """
        return self.title