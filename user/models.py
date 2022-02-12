from django.db import models


class User(models.Model):
    user_name = models.CharField('', max_length=20)
    user_id = models.CharField('', max_length=20, primary_key=True)
    user_pw = models.TextField('', max_length=500, default=None)
    user_email = models.EmailField('', max_length=128, default=None)
    is_social = models.BooleanField(default=False)

    def __str__(self):
        return self.user_id



