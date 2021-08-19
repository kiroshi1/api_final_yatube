from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments')
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),
]
