"""Generated from Smithy shape ``com.amazonaws.finspacedata#UserByPermissionGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_finspace_data.types.user_by_permission_group

UserByPermissionGroupList: TypeAlias = list[
    "capo_finspace_data.types.user_by_permission_group.UserByPermissionGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: UserByPermissionGroupList) -> list:
    import capo_finspace_data.types.user_by_permission_group

    out: list = []
    for item in value:
        out.append(
            capo_finspace_data.types.user_by_permission_group.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> UserByPermissionGroupList:
    import capo_finspace_data.types.user_by_permission_group

    out: UserByPermissionGroupList = []
    for item in data:
        out.append(
            capo_finspace_data.types.user_by_permission_group.deserialize_json(item)
        )
    return out
