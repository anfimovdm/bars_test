from app import ui as dev_ui
from objectpack import actions, ui
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from .controller import observer


class UserPack(actions.ObjectPack):
    model = User
    add_window = edit_window = dev_ui.UserAddEditWindow
    add_to_menu = True
    add_to_desktop = True


class GroupPack(actions.ObjectPack):
    model = Group
    add_window = edit_window = ui.ModelEditWindow.fabricate(model,
                                                            model_register=observer)
    add_to_menu = True
    add_to_desktop = True


class ContentPack(actions.ObjectPack):
    model = ContentType
    add_window = edit_window = ui.ModelEditWindow.fabricate(model,
                                                            model_register=observer)
    add_to_menu = True
    add_to_desktop = True


class PermissionPack(actions.ObjectPack):
    model = Permission
    add_window = edit_window = ui.ModelEditWindow.fabricate(model,
                                                            model_register=observer)

    add_to_menu = True
    add_to_desktop = True
