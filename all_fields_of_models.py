from django.db.models import get_app, get_models

app = get_app('my_application_name')
  for model in get_models(app):
    print model, model._meta.get_all_field_names()
