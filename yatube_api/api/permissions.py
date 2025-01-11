from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    """Пермишн для работы с коллекцией объектов."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class ReadOnly(permissions.BasePermission):
    """Пермишн для работы с отдельным объектом."""

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
