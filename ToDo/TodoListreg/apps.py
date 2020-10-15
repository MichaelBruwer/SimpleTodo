from django.apps import AppConfig


class TodolistregConfig(AppConfig):
    name = 'TodoListreg'

    def ready(self):
        import TodoListreg.signals