from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

class Movie(models.Model):
    title = models.CharField(max_length=32)
    desc = models.CharField(max_length=256)
    year = models.IntegerField(
            validators=[
                MinValueValidator(1900),
                MaxValueValidator(datetime.datetime.now().year)],
            help_text="Use the following format: <YYYY>")
