from django.conf.urls import url, include

from .views import CreateUserView, SecretView


urlpatterns = [
    url(r'^secret/$', view=SecretView.as_view()),
]
