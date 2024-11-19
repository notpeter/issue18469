from django.db import models


def test():
    print(Person.objects.all())
    return


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
