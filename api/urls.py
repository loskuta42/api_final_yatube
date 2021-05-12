from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import (
    CommentViewSet,
    FollowViewSet,
    GroupViewSet,
    PostViewSet
)


router = DefaultRouter()
router.register(
    'v1/posts',
    PostViewSet,
    basename='Post'
)
router.register(
    'v1/group',
    GroupViewSet,
    basename='Group'
)
router.register(
    r'v1/posts/(?P<id>[0-9]+)/comments',
    CommentViewSet,
    basename='Comment'
)
router.register(
    'v1/follow',
    FollowViewSet,
    basename='Follow'
)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'v1/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'v1/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
]
