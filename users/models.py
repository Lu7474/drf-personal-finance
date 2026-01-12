from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)

    # Указываем, что email является уникальным идентификатором
    USERNAME_FIELD = "email"
    # Список полей, которые запрашиваются при создании через createsuperuser
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        # Если email есть, а username не задан, копируем его
        if self.email and not self.username:
            self.username = self.email
        super().save(*args, **kwargs)
