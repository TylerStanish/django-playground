from django.conf.urls import url, include

from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from .views import CreateUserView, LogoutView, SecretView


urlpatterns = [
    url(r'^login/$', view=obtain_jwt_token),
    url(r'^refresh-token/$', refresh_jwt_token),
    url(r'^create_account/$', view=CreateUserView.as_view()),
    url(r'^logout/$', view=LogoutView.as_view()),
    url(r'^secret/$', view=SecretView.as_view()),
]
