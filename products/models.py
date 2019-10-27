from django.db import models


class Chair(models.Model):
    model_number = models.CharField(max_length=20)
    model_image = models.ImageField(upload_to='images/')


class Feature(models.Model):
    feature_image = models.ImageField(upload_to='images/')
    chair = models.ForeignKey(Chair, on_delete=models.CASCADE)

