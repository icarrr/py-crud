## Register Model In Django Admin
# from django.contrib import admin
# from .models import Task
# admin.site.register(Task)

# Register All Models In Django Admin(Same App)
from django.contrib import admin
from django.apps import apps
todoapp_models = apps.get_app_config('todoApp').get_models()
for model in todoapp_models:
    try:
        admin.site.register(model)
    except admin.site.AlreadyRegistered:
        pass