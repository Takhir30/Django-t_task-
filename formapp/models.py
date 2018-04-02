from django.contrib.postgres.fields import JSONField
from django.db import models


class Inputs(models.Model):
    input_text = JSONField()
