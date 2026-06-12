"""Generated from Smithy shape ``com.amazonaws.finspacedata#PermissionGroupByUserList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.permission_group_by_user

PermissionGroupByUserList: TypeAlias = list[
    "aws_sdk_finspace_data.types.permission_group_by_user.PermissionGroupByUser"
]


# --- restJson1 ser/de ---
def serialize_json(value: PermissionGroupByUserList) -> list:
    import aws_sdk_finspace_data.types.permission_group_by_user

    out: list = []
    for item in value:
        out.append(
            aws_sdk_finspace_data.types.permission_group_by_user.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PermissionGroupByUserList:
    import aws_sdk_finspace_data.types.permission_group_by_user

    out: PermissionGroupByUserList = []
    for item in data:
        out.append(
            aws_sdk_finspace_data.types.permission_group_by_user.deserialize_json(item)
        )
    return out
