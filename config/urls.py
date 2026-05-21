from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'api/v1/',
        include('blog.urls')
    ),
    path(
        'token/',
        TokenObtainPairView.as_view()
    ),

    path(
        'token/refresh/',
        TokenRefreshView.as_view()
    ),
    path(
        'api/schema/',
        SpectacularAPIView.as_view()
    ),

    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(
            url_name='schema'
        )
    ),
]
