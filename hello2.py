from django.db import models
from django.utils.functional import cached_property


class Friend:

    def add_new_friend(self, person_id):
        print("add new friend")


# Create your models here.
class Person(models.Model):
    id = models.AutoField(primary_key=True)

    @cached_property
    def friend(self):
        return Friend()

    def add_me_to_friend_list(self):
        self.friend.add_new_friend(self.id)
