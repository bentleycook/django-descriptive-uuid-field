# -*- coding: utf-8 -*-
import string
import uuid

from django.db.models import UUIDField


class DescriptiveUUIDField(UUIDField):
    description = 'Universally unique identifier'

    def __init__(self, prefix=None, auto=True, *args, **kwargs):
        if not prefix:
            raise ValueError(
                "The 'prefix=' argument is a required keyword argument.")
        else:
            self.prefix = prefix
        super(DescriptiveUUIDField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(
            DescriptiveUUIDField, self).deconstruct()

        kwargs['prefix'] = self.prefix

        return name, path, args, kwargs

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return f'{self.prefix}{value}'

    def get_prep_value(self, value):
        if self.prefix in value:
            return value[len(self.prefix):]
        return value

    def get_db_prep_value(self, value, connection, prepared=False):
        value = super().get_db_prep_value(value, connection, prepared)
        return value

    def to_python(self, value):
        if value is None:
            return value
        new_value = value
        if self.prefix in new_value:
            new_value = new_value[len(self.prefix):]
        return uuid.UUID(new_value).hex
