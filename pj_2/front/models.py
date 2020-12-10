from django.db import models


class Thems(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name


    def Meta(self):
        db_table = 'front_thems'

