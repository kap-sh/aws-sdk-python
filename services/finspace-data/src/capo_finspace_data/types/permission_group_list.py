"""Generated from Smithy shape ``com.amazonaws.finspacedata#PermissionGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_finspace_data.types.permission_group

PermissionGroupList: TypeAlias = list[
    "capo_finspace_data.types.permission_group.PermissionGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionGroupList) -> list:
    import capo_finspace_data.types.permission_group

    out: list = []
    for item in value:
        out.append(capo_finspace_data.types.permission_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> PermissionGroupList:
    import capo_finspace_data.types.permission_group

    out: PermissionGroupList = []
    for item in data:
        out.append(capo_finspace_data.types.permission_group.deserialize_json(item))
    return out
