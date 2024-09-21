from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('newapp.urls')),  # 包含 myapp 的 URL 配置
]
