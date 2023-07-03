from . import views
from django.urls import path

app_name='app'

urlpatterns=[
    path("",views.purple,name="purple"),
    path("charts",views.charts,name="charts"),
    path("forms",views.forms,name="forms"),
    path("mdi",views.icons,name="icons"),
    path("login",views.login,name="login"),
    path("register",views.register,name="register"),
    path("tables",views.tables,name="tables"),
    path("buttons",views.buttons,name="buttons"),
    path("typography",views.typography,name="typography"),

]