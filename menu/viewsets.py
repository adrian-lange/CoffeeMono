from rest_framework.viewsets import ModelViewSet
from authx.permissions import MenuViewPermission


from .serializers import (
    CreateMenuItemSerializer,
    CreateMenuSerializer,
    CreateComponentSerializer,
    MenuSerializer,
    CashierMenuSerializer,
    MenuItemSerializer,
    ComponentSerializer,
    ManagerComponentSerializer,
    AdminMenuSerializer,
    CashierMenuItemSerializer,
    ManagerMenuItemSerializer,
    MenuItemSerializer,
)
from .models import Menu, MenuItem, Component

from utils.mixins import CustomLoggingViewSetMixin


class MenuView(CustomLoggingViewSetMixin, ModelViewSet):

    queryset = Menu.objects.all()
    permission_classes = [MenuViewPermission]

    def get_serializer_class(self):
        if self.request.user.role == 1:
            return CashierMenuSerializer
        elif self.request.user.role >= 3:
            if self.action in ['update', 'partial_update', 'create']:
                return CreateMenuSerializer
            return AdminMenuSerializer
        else:
            if self.action in ['update', 'partial_update', 'create']:
                return CreateMenuSerializer
            return MenuSerializer


class MenuItemView(CustomLoggingViewSetMixin, ModelViewSet):

    queryset = MenuItem.objects.all()
    permission_classes = [MenuViewPermission]

    def get_serializer_class(self):
        if self.request.user.role == 1:
            return CashierMenuItemSerializer
        elif self.request.user.role >= 3:
            if self.action in ['update', 'partial_update', 'create']:
                return CreateMenuItemSerializer
            return ManagerMenuItemSerializer
        else:
            if self.action in ['update', 'partial_update', 'create']:
                return CreateMenuItemSerializer
            return MenuItemSerializer


class ComponentView(CustomLoggingViewSetMixin, ModelViewSet):

    queryset = Component.objects.all()
    permission_classes = [MenuViewPermission]

    def get_serializer_class(self):
        
        if self.request.user.role >= 3:
            if self.action in ['update', 'partial_update', 'create']:
                return CreateComponentSerializer
            return ManagerComponentSerializer
        else:
            return ComponentSerializer
