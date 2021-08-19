from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import filters
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from posts.models import Group, Post, Follow, User

from .serializers import CommentSerializer, GroupSerializer, PostSerializer, FollowSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwner, ]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwner, ]
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        queryset = post.comments.all()
        return queryset

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, )
    search_fields = ['user__username', 'following__username']
    queryset = Follow.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = FollowSerializer

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        user = get_object_or_404(User, username=self.request.data['following'])
        serializer.save(user=self.request.user, following=user)
