from django.db import models


# Create your models here.
class Rockets(models.Model):
    rocket_id = models.CharField(max_length=200)
    rocket_name = models.CharField(max_length=200)
    rocket_type = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    stages = models.IntegerField(default=0)
    boosters = models.IntegerField(default=0)
    cost_per_launch = models.FloatField(default=0)

    success_rate_pct = models.IntegerField(default=0)
    country = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    wikipedia = models.CharField(max_length=200)
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.rocket_name
