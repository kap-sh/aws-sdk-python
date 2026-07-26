"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomPermissionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.custom_permissions

CustomPermissionsList: TypeAlias = list[
    "capo_quicksight.types.custom_permissions.CustomPermissions"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomPermissionsList) -> list:
    import capo_quicksight.types.custom_permissions

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.custom_permissions.serialize_json(item))
    return out


def deserialize_json(data: list) -> CustomPermissionsList:
    import capo_quicksight.types.custom_permissions

    out: CustomPermissionsList = []
    for item in data:
        out.append(capo_quicksight.types.custom_permissions.deserialize_json(item))
    return out
