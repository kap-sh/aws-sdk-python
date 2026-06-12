"""Generated from Smithy shape ``com.amazonaws.finspacedata#UserByPermissionGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.user_by_permission_group

UserByPermissionGroupList: TypeAlias = list[
    "aws_sdk_finspace_data.types.user_by_permission_group.UserByPermissionGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: UserByPermissionGroupList) -> list:
    import aws_sdk_finspace_data.types.user_by_permission_group

    out: list = []
    for item in value:
        out.append(
            aws_sdk_finspace_data.types.user_by_permission_group.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> UserByPermissionGroupList:
    import aws_sdk_finspace_data.types.user_by_permission_group

    out: UserByPermissionGroupList = []
    for item in data:
        out.append(
            aws_sdk_finspace_data.types.user_by_permission_group.deserialize_json(item)
        )
    return out
