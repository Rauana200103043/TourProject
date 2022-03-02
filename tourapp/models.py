from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    surname = models.CharField(max_length=255, db_index=True)
    gender = models.CharField(max_length=20, db_index=True)
    country_id = models.CharField(max_length=20, db_index=True)

    class Meta:
        verbose_name = 'Users'
        verbose_name_plural = 'Users'
        ordering = ['id']
