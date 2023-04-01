from django.db import models
from django.contrib.auth import get_user_model


class Theme(models.Model):
    author = models.ForeignKey(
        null=False,
        blank=False,
        to=get_user_model(),
        related_name='topics',
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )

    name = models.CharField(
        max_length=256,
        null=False,
        blank=False,
        verbose_name='Название',
    )

    text = models.TextField(
        max_length=2048,
        null=True,
        blank=True,
        verbose_name='Описание',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f'Theme: {self.name}, Author: {self.author}'

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
