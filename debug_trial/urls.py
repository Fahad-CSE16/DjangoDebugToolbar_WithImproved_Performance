from django.contrib import admin
from django.urls import path, include
from blogpost.views import *
import debug_toolbar
urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('',homeView),
]
