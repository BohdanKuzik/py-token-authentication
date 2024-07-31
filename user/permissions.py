from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view=None):
        return bool(
            request.user.is_staff and request.user.is_authenticated
        ) or (
            request.method in SAFE_METHODS
            and request.user
            and request.user.is_authenticated
        )