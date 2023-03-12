from django.db import models


class school(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=20)
    pin_code = models.CharField(max_length=10)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class sutudent(models.Model):
    name = models.CharField(max_length=20, default=None, editable=True)
    user_name = models.CharField(max_length=4, unique=True)
    password = models.CharField(max_length=15)
    grade = models.PositiveSmallIntegerField()
    school = models.CharField(max_length=200)

    # def __str__(self):
    #     return self.grade
