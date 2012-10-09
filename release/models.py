from django.db import models

# Create your models here.
class release(models.Model):
    releaseName=models.CharField(max_length=20);
    estimate=models.ForeignKey()
