from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

api_v1_router = DefaultRouter()
api_v1_router.register('posts', PostViewSet)
api_v1_router.register('groups', GroupViewSet)
api_v1_router.register('follow', FollowViewSet, basename='follow')

comment_router = DefaultRouter()
comment_router.register('comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('v1/', include(api_v1_router.urls)),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/posts/<int:post_id>/', include(comment_router.urls))
]
