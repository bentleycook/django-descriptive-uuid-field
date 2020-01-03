# -*- coding: utf-8 -*-
from django.db import models

from descriptive_uuid_field.fields import DescriptiveUUIDField


class MyModel(models.Model):
    number = DescriptiveUUIDField(prefix='human_')
