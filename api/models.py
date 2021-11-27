from django.db import models


class DataArduino(models.Model):
    vazao = models.FloatField()
    date = models.DateTimeField()
