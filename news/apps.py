from django.apps import AppConfig


class NewsConfig(AppConfig):
    name = 'news'
    verbose_name = 'Новости'

class CategoryConfig(AppConfig):
    verbose_name = 'Категории'
