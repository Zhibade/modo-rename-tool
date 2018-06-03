#python
# Rename tool
# Replace text in item's names and/or add a suffix/prefix
# Author: Jose Lopez Romo - Zhibade

import modo, renametool_utils

# UI Values

OLD_NAME = renametool_utils.query_user_value('zbRenameTool_oldName')
NEW_NAME = renametool_utils.query_user_value('zbRenameTool_newName')
PREFIX = renametool_utils.query_user_value('zbRenameTool_prefix')
SUFFIX = renametool_utils.query_user_value('zbRenameTool_suffix')

RENAME_SELECTED_ONLY = renametool_utils.query_user_value('zbRenameTool_renameSelected')
SHOULD_RENAME = renametool_utils.query_user_value('zbRenameTool_shouldRename')
ADD_PREFIX = renametool_utils.query_user_value('zbRenameTool_addPrefix')
ADD_SUFFIX = renametool_utils.query_user_value('zbRenameTool_addSuffix')

# Initialization

scene = modo.Scene()

# Functions

def rename_selected(replace_str, new_str):
    """
    Renames selected items only

    Params:
        replace_str :: String - Old name to replace
        new_str :: String - New name
    """

    selected = scene.selected

    if not selected:
        modo.dialogs.alert("Warning", "No objects selected. Please select at least one object.", 'warning')

    for obj in selected:
        if SHOULD_RENAME:
            rename_object(obj, obj.name.replace(replace_str, new_str))

        handle_suffix_prefix(obj)


def rename_all(replace_str, new_str):
    """
    Renames all scene items

    Params:
        replace_str :: String - Old name to replace
        new_str :: String - New name
    """

    confirmation = modo.dialogs.yesNo("Are you sure?", "All items in the scene will be renamed. Would you like to continue?")

    if confirmation != "yes":
        sys.exit()

    all_items = scene.items()

    for obj in all_items:
        if SHOULD_RENAME:
            rename_object(obj, obj.name.replace(replace_str, new_str))

        handle_suffix_prefix(obj)


def handle_suffix_prefix(obj):
    """
    Adds prefix and/or suffix to passed object

    Params:
        obj :: MODO Item - Object to add prefix/suffix
    """

    if ADD_PREFIX:
        rename_object(obj, PREFIX + obj.name)

    if ADD_SUFFIX:
        rename_object(obj, obj.name + SUFFIX)


def rename_object(obj, new_name):
    obj.select(True)
    lx.eval('item.name "{0}"'.format(new_name)) # Have to rename with lx.eval otherwise undo doesn't work

# Main

if RENAME_SELECTED_ONLY:
    rename_selected(OLD_NAME, NEW_NAME)
else:
    rename_all(OLD_NAME, NEW_NAME)
