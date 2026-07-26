"""Generated from Smithy shape ``com.amazonaws.finspacedata#ResourcePermissionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_finspace_data.types.resource_permission

ResourcePermissionsList: TypeAlias = list[
    "capo_finspace_data.types.resource_permission.ResourcePermission"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcePermissionsList) -> list:
    import capo_finspace_data.types.resource_permission

    out: list = []
    for item in value:
        out.append(capo_finspace_data.types.resource_permission.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourcePermissionsList:
    import capo_finspace_data.types.resource_permission

    out: ResourcePermissionsList = []
    for item in data:
        out.append(capo_finspace_data.types.resource_permission.deserialize_json(item))
    return out
