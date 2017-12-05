from django.apps import AppConfig

class AuthenticationAppConfig(AppConfig):
    name = 'conduit.apps.authentication'
    label = 'authentication'
    verbose_name = 'Authentication'

    def ready(self):
        import conduit.apps.authentication.signals


default_app_config = 'conduit.apps.authentication.AuthenticationAppConfig'
