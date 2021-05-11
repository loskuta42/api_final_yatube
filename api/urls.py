from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CommentViewSet,
    FollowViewSet,
    GroupViewSet,
    PostViewSet
)


router = DefaultRouter()
router.register(
    'posts',
    PostViewSet,
    basename='Post'
)
router.register(
    'group',
    GroupViewSet,
    basename='Group'
)
router.register(
    r'posts/(?P<id>[0-9]+)/comments',
    CommentViewSet,
    basename='Comment'
)
router.register(
    'follow',
    FollowViewSet,
    basename='Follow'
)

urlpatterns = [
    path('', include(router.urls))
]
